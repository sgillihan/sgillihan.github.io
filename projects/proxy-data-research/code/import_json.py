from __future__ import annotations

from pathlib import Path
import json
import gzip
from typing import Iterable, Iterator, Optional, Union
import pandas as pd

def _open_text(path:Path, encoding: str = "utf-8"):
    """Open .json/.jsol or .gz equivalent as text stream."""
    if path.suffix.lower() == ".gz":
        return gzip.open(path, mode="rt", encoding=encoding, errors="replace")
    return open(path, "rt", encoding=encoding, errors="replace")

def _auto_detect_lines(path: Path, encoding: str = "utf-8", sniff_lines: int = 50) -> bool:
    """
    .json/.ndjson => lines
    else sniff first non-empty line: if it begins with { or [, assume standard JSON.
    otherwise assume JSONL/NDJSON
    """
    suffixes = "".join(path.suffixes).lower()
    if suffixes.endswith(".jsonl") or suffixes.endswith(".ndjson") or path.suffix.lower() in {".jsonl",".ndjson"}:
        return True
    
    with _open_text(path, encoding=encoding) as f:
        for _ in range(sniff_lines):
            line = f.readline()
            if not line:
                break
            s = line.strip()
            if not s:
                continue
            return not (s.startswith("{") or s.startswith("["))  # if starts with { or [, assume standard JSON
    return False  # default to standard JSON if no non-empty lines found

def _extract_by_path(obj, record_path: Union[str, list[str]]):
    """Navigate nested dict keys like['Browser History']."""
    if isinstance(record_path, str):
        record_path = [record_path]
    cur = obj
    for key in record_path:
        if not isinstance(cur, dict) or key not in cur:
            raise KeyError(f"Key '{key}' not found while navigating record_path.")
        cur = cur[key]
    return cur

def load_json_to_df(
        path: str | Path,
    *,
    lines: bool | None = None,
    chunksize: int | None = None,
    record_path: Union[str, list[str], None] = None,
    meta: Optional[list[str]] = None,
    encoding: str = "utf-8",
    **read_json_kwargs,
) -> Union[pd.DataFrame, Iterator[pd.DataFrame]]:
    """
    General JSON -> DataFrame loader.

    Supports:
    - Standard JSON (.json): list/dict. (Loads whole file into memory.)
    - JSONL/NDJSON (.jsonl/.ndjson): streaming with chunksize.
    - Gzip versions: .json.gz, .jsonl.gz

    Parameters
    ----------
    path:
        File path.
    lines:
        True for JSONL/NDJSON. If None, auto-detect.
    chunksize:
        If provided AND lines=True, returns an iterator of DataFrames.
    record_path:
        For standard JSON: extract nested list by dict key path (e.g., "Browser History" or ["a","b"]).
        For JSONL: typically leave None because each line is already a record.
    meta:
        Passed to pd.json_normalize for standard JSON only (optional).
    read_json_kwargs:
        Passed to pandas.read_json when lines=True.

    Returns
    -------
    DataFrame or iterator[DataFrame]
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"JSON file not found: {p}")

    if lines is None:
        lines = _auto_detect_lines(p, encoding=encoding)

    # --- JSONL/NDJSON path: scalable ---
    if lines:
        # pandas can stream JSONL efficiently with chunksize
        return pd.read_json(
            p,
            lines=True,
            chunksize=chunksize,
            encoding=encoding,
            **read_json_kwargs,
        )

    # --- Standard JSON path: loads whole object ---
    # This is the inherent limitation of monolithic JSON.
    with _open_text(p, encoding=encoding) as f:
        obj = json.load(f)

    if record_path is not None:
        records = _extract_by_path(obj, record_path)
        return pd.json_normalize(records, meta=meta or [])
    else:
        # Try to normalize nested structures; fall back to DataFrame
        try:
            return pd.json_normalize(obj)
        except Exception:
            return pd.DataFrame(obj)
        
"""
Example usage:
#standard JSON with nested list:
from import_json import load_json_to_df

history_path = r"C:\...\Takeout\Chrome\History.json"
df = load_json_to_df(history_path, record_path="Browser History")
print(df.shape)
print(df.columns[:20])


#Huge JSONL with chunking:
chunks = load_json_to_df("big.jsonl", lines=True, chunksize=200_000)

first = next(chunks)
print(first.columns)

# Example: compute a count without loading it all
total = 0
for chunk in chunks:
    total += len(chunk)
print("rows:", total)

#write headers:
df0 = load_json_to_df(history_path, record_path="Browser History").head(0)
df0.columns.to_series().to_csv("history_headers.csv", index=False, header=["column_name"])


"""