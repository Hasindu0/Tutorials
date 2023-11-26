convert = input("Enter your choice: ")
temp = float(input("Enter temperature: "))
if convert == '1':
    fahrenheit = (temp * 1.8) + 32
    print(temp,"Celsius is equal to",fahrenheit,"Fahrenheit.")
elif convert == '2':
    celsius = (temp - 32) / 1.8
    print(temp,"Fahrenheit is equal to",celsius,"Celsius.")
else:
    print("Invalid option entered.")
