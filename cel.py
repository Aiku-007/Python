def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))

cel_to_fahren=int(input("Enter the value in celsius: "))
print("The value from celsius to farenheit is",celsius_to_fahrenheit(cel_to_fahren))