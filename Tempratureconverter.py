temp = float(input("Enter the temprature: "))
print("select a unit of choice from the list given below: ")
print("a. Celsius")
print("b. Fahrenheit")
print("c. Kelvin")

unit = input("Enter The choice: ")

if unit == 'a':
    celsius = temp
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    print("temprature in celsius is:", celsius)
    print("temprature in fahrenheit is:", fahrenheit)
    print("tempratre in kelvin is:", kelvin)
elif unit == 'b':
    fahrenheit = temp
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    print("temprature in fahrenheit is:", temp)
    print("temprature in celsius is:", celsius)
    print("temprature in kelvin is:", kelvin)
elif unit == 'c':
    kelvin = temp
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print("temprature in kelvin is:", temp)
    print("temprature in celsius is:", celsius)
    print("temprature in fahrenheit is:", fahrenheit)
else:
    print("You have enter the wrong choice.")
