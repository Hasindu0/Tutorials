pizza='Hawaiian'
print(pizza[0])
print(pizza[:5])
print(pizza[0:2])
print("pizza[6]")
print(pizza)
print(pizza[6])
print(pizza[2:4])
print(pizza[3:])
print(pizza[-1])
print(pizza[:-1])

############

full_name = input("Enter your full name: ")

print("The whole name:", full_name)
print("The first character:", full_name[0])
print("The first 5 characters:", full_name[:5])
print("The fourth, fifth, and sixth characters:", full_name[3:6])

##############################

username = input("Enter a username of 6 characters: ")
if len(username) == 6:
    print("You entered a username with 6 characters.")
else:
    print("The username should be exactly 6 characters.")
