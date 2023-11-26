#if
n = int(input('Give me a number over 100: '))
if n <= 100:
 print(n, 'is not over 100')

age = int(input("Enter your age: "))
if age >= 18:
    print("Can vote")

#if- else
x = int(input('Give me a number: '))
if x < 0:
 print(x, 'is negative')
else:
 print(x, 'is positive')

marks=int(input("Enter your marks:"))
if marks<40:
    print("Fail")
else:
    print("Pass")

number = int(input("Enter the number: "))
if number%2==0:
    print("Even number")
else:
    print("Odd number")
