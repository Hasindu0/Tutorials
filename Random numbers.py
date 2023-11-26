import random
secret_number = random.randint(1,20)
print(secret_number)

num2=random.randint(1, 4)
print(num2)

print("Coin is spining")
coin=random.randint(0,1)
if coin==0:
    print("Heads")
else:
    print("Tail")
