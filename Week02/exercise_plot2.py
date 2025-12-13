import pandas as pd
import matplotlib.pyplot as plt
Temperature = [65, 68, 75, 80, 85]

City = ["Seattle", "Lahore",  "Newyork", "Karachi", "Multan"]
Colours = ["green", "Red", "Pink", "Purple", "black"]
plt.bar(City, Temperature, color=Colours)
plt.title("Bar Chart")
plt.xlabel("City")
plt.ylabel("Temperature")
plt.show()
