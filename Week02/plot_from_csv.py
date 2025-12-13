import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sample_data.csv")
plt.plot(df["Name"], df["Temperature"])
plt.title("first plot")
plt.xlabel("Name")
plt.ylabel("Temperature")
plt.show()
