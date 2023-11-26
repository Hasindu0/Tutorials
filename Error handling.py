n = input("Please enter an integer: ")
try:
 n = int(n)
 print(n)
except ValueError:
 print("Requires a valid integer!")

try:
    x = 45 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')

