# This utility function allows loading CSV files directly from a ZIP archive without needing to extract them first.
# It supports both loading a specific CSV by name and concatenating all CSVs in the ZIP. Additionally, it can return an iterator for chunked reading if a chunksize is specified.
# Written with ChatGPT v 5.2
from pathlib import Path
import zipfile
import pandas as pd

def load_csv_from_zip(zip_path, csv_filename=None, concat_all=False, **read_csv_kwargs):
    """
    Load CSV file(s) from a ZIP archive.

    Behavior:
    - If chunksize is provided in read_csv_kwargs, returns an iterator (TextFileReader) for ONE CSV.
    - If concat_all=True (and no chunksize), reads all CSVs and concatenates them.

    Parameters
    ----------
    zip_path : str | Path
        Path to the ZIP file.
    csv_filename : str | None
        CSV filename to load. Can be exact internal path OR just basename.
        If None and concat_all=False, loads the first CSV found.
    concat_all : bool
        If True, loads all CSVs in the ZIP and concatenates them (not recommended for huge datasets).
    read_csv_kwargs :
        Passed directly to pandas.read_csv (e.g., low_memory, usecols, dtype, chunksize, etc.)
    """
    zip_path = Path(zip_path)
    if not zip_path.exists():
        raise FileNotFoundError(f"ZIP file not found: {zip_path}")

    chunksize = read_csv_kwargs.get("chunksize", None)
    if chunksize is not None and concat_all:
        raise ValueError("chunksize + concat_all=True isn't supported (concat would defeat chunking).")

    with zipfile.ZipFile(zip_path) as z:
        csv_files = [f for f in z.namelist() if f.lower().endswith(".csv")]
        if not csv_files:
            raise ValueError(f"No CSV files found inside {zip_path.name}")

        # pick target files
        if concat_all:
            target_files = csv_files
        else:
            if csv_filename is None:
                target_files = [csv_files[0]]
                print(f"No CSV filename specified. Loading first CSV found: {Path(target_files[0]).name}")
            else:
                matches = [
                    f for f in csv_files
                    if f == csv_filename or Path(f).name == csv_filename
                ]
                if len(matches) != 1:
                    available = "\n".join(Path(f).name for f in csv_files)
                    raise ValueError(
                        f"CSV '{csv_filename}' not found uniquely in {zip_path.name}.\n"
                        f"Available CSVs:\n{available}"
                    )
                target_files = matches

        # If chunking, only support one CSV at a time and return iterator
        if chunksize is not None:
            if len(target_files) != 1:
                raise ValueError("When using chunksize, load exactly one CSV (set concat_all=False).")
            target = target_files[0]
            f = z.open(target)  # keep zip open while iterator is used
            return pd.read_csv(f, **read_csv_kwargs)

        # Non-chunking path: read fully into memory
        dfs = []
        for file in target_files:
            with z.open(file) as f:
                dfs.append(pd.read_csv(f, **read_csv_kwargs))

        return pd.concat(dfs, ignore_index=True) if len(dfs) > 1 else dfs[0]
