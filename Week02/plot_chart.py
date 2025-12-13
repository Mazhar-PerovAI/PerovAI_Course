import matplotlib.pyplot as plt

Players = ["Imran", "Waseem", "Dhoni", "Bhatti" ]
Runs = [100, 85, 105, 45]

colours = ["red", "blue", "green", "grey"]

plt.bar(Players, Runs, color=colours)
plt.title("Runs of Players")
plt.xlabel("Players")
plt.ylabel("Runs")
plt.show()

