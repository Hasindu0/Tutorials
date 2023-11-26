num1 = float(input("Enter the first number: "))
operator = input("Enter an operator: ")
num2 = float(input("Enter the second number: "))


if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2==0:
        print("Can not devided by zero")
        exit()
    else:
        result = num1 / num2
    
print("Result is:",result)
#########

num1 = float(input("Enter the first number: "))
operator = input("Enter an operator: ")
num2 = float(input("Enter the second number: "))


if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Can not devided by zero")
        exit()
    
print("Result is:",result)
