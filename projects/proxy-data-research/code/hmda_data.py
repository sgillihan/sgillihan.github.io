import pandas as pd
from pathlib import Path
import numpy as np
from import_csv_from_zip import load_csv_from_zip

zip_path = r"C:\Users\User\OneDrive\Documents\CSPB3112\Datasets\HMDA\hmda_2017_nationwide_all-records_labels.zip"

# Load just the header to inspect column names and types
df_header = load_csv_from_zip(
    zip_path,
    nrows=0
)
print(df_header.columns.tolist())

headers_df = df_header.columns.to_series()
headers_df.to_csv("hmda_2017_headers.csv", index=False, header=["column_name"])


# #HMDA data
# chunks = load_csv_from_zip(zip_path, lchunksize=100_000, low_memory=True)

# filtered_parts = []
# for chunk in chunks:
#     # adjust column name to what your file actually uses
#     col_name = "loan_amount"  # example column name
#     if col_name in chunk.columns:
#         chunk = chunk[chunk[col_name] == 100_000]
#     filtered_parts.append(chunk)


# df = pd.concat(filtered_parts, ignore_index=True)
# print(df.shape)
# print(df.columns[:10])
# print(df.dtypes.head())
# print(df.head())


# # Example of calculating mean loan amount using chunking to avoid memory issues
# total_sum = 0
# total_count = 0

# chunks = load_csv_from_zip(
#     zip_path,
#     chunksize=100_000,
#     usecols=["loan_amount"],
#     low_memory=True
# )

# for chunk in chunks:
#     total_sum += chunk["loan_amount"].sum()
#     total_count += chunk["loan_amount"].count()

# mean_loan = total_sum / total_count
# print(mean_loan)
