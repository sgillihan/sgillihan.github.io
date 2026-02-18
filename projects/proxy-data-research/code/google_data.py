# This code with explore the cleaned google browser history data, and do some basic EDA and visualization.
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from import_json import load_json_to_df

data_path1 = Path(r"C:/Users/User/OneDrive/Documents/CSPB3112/Datasets/Personal_Google/Takeout/Chrome/History.json")
data_path2 = Path(r"C:/Users/User/OneDrive/Documents/CSPB3112/Datasets/Personal_Google/Takeout/Chrome/Device Information.json")

df_chrome_hist = load_json_to_df(data_path1)
df_chrome_hist.to_parquet(r"C:\Users\User\OneDrive\Documents\CSPB3112\Datasets\Personal_Google\chrome_history_cleaned.parquet",
    index=False)

df_device_info = load_json_to_df(data_path2)
df_device_info.to_parquet(r"C:\Users\User\OneDrive\Documents\CSPB3112\Datasets\Personal_Google\device_info_cleaned.parquet",
    index=False)

