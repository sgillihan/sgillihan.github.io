# This code with explore the cleaned google browser history data, and do some basic EDA and visualization.
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_path = Path(r"C:/Users/User/OneDrive/Documents/CSPB3112/Datasets/Personal_Google/processed/chrome_history_cleaned.parquet")

df = pd.read_parquet(data_path)

