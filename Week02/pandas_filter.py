import pandas as pd

df = pd.read_csv("sample_data.csv")

adults = df[df["Age"] > 30]
print(adults)

print(df.describe()) # statistics 

print(df.head()) # first rows 
print(df.tail()) # last rows 
print(df.info()) # data structure 