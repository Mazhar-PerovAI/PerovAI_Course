import pandas as pd

df = pd.read_csv("sample2_data.csv")

good = df[df["PCE"] > 24]
print("good")