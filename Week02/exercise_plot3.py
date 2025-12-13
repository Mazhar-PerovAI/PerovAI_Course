import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sample_data.csv")
colours = ("red", "green", "yellow", "black")
plt.scatter(df["Name"], df["Age"], color=colours, marker="o")
plt.title("scattered plot")
plt.xlabel("Name")
plt.ylabel("Age")
plt.show()