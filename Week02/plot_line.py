import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temperature = [68, 70, 72, 71, 69]
plt.plot(days, temperature)
plt.xlabel("days")
plt.ylabel("temperature")
plt.title("Temperature over Days")

plt.grid("false")
         
plt.show()