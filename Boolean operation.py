#and
m = int(input('Give me number between 1 and 10:'))
if m>=1 and m< 11:
    print('Well done! You gave me: ',m)

#or

marks=int(input("Enter your marks:"))
if marks<0 or marks>100:
    print("Invalid marks")
elif marks >= 70:
    print("Exceptional result!")
elif marks >= 40:
    print("Satisfactory result!")
else:
    print("You have failed.")

#not
x = 10
if not x > 10:
 print("not returned True")
else:
 print("not returned False")
##########################

response = input('Do you like Python? (yes,Yes,y/no,No,n): ')
response = response.lower()

if response == 'yes' or response == 'y':
    print('You are on the right course!')
elif response == 'no' or response == 'n':
    print('You might change your mind.')
else:
    print('I did not understand your response.')


