# ćwiczenie z podręcznika
import ssl
import warnings
import pandas as pd

warnings.filterwarnings('ignore')
ssl._create_default_https_context = ssl._create_unverified_context
import requests as req # pyright: ignore[reportMissingModuleSource]
from io import StringIO

url = "https://raw.githubusercontent.com/kflisikowsky/sad/refs/heads/main/data/billboard_analysis.csv"
response = req.get(url, verify=False)
df_lyrics = StringIO(response.text)
df_lyrics = pd.read_csv(df_lyrics, sep=",")
print(df_lyrics.head(3))