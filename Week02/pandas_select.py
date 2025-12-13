import pandas as pd

df = pd.DataFrame({
    "Name": ["Mazhar", "Ali", "Sara"],
    "Age": [43, 30, 25],
    "City": ["Seattle", "Lahore", "Karachi"]
})

print(df["Name"])
print(df[["Name", "City"]])