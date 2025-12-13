def c_to_f(c):
    return c * 9/5 + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = c_to_f(celsius)
print("Fahrenheit:", fahrenheit)