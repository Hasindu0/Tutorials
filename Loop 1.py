import random
hidden = random.randint(1,20)

guess = int(input("Enter a guess (between 1 and 20): "))

while guess != hidden:
    print("Incorrect guess. Try again.")
    if hidden<guess:
        print ("Too high")
    else:
        print("Too low")
    guess = int(input("Enter the next guess (between 1 and 20): "))
print("Your guess is correct.")
