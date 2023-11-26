#4
total = 0
for i in range(5):
    print(i,end=' ')
    total += i
print("\nThe total of the 5 numbers is:",total)

#5
for number in range(1, 21, 2):
    print(number)

#6

num_stars = int(input("Enter the number of stars you want: "))

for s in range(num_stars):
    print("*", end=" ")
print()
    
#7

import random

count = 0

for c in range(100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 == dice2:
        count += 1

print("Out of 100 rolls doubles are:",count,"times.")


