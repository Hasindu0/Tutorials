try:
    n = input('Give me a number over 100: ')
    n = int(n)
    if n <= 100:
        print(n, 'is not over 100')
except ValueError:
    print("Invalid input")

try:
    age = input('Enter your age: ')
    age = int(age)
    if age >= 18:
        print("You can vote")
except ValueError:
    print("Invalid Input")
