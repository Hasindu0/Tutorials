str_value = 'cosc001W'

print("Original String:", str_value)
print("Uppercase:", str_value.upper())
print("Lowercase:", str_value.lower())
print("Capitalized:", str_value.capitalize())

print()

line = ' more white space '
print(line)
print(line.strip())
print(line)

print()

line = ' lots of white space '
print(line)
line = line.strip()
print(line)

print()

guesses = 'abcde'
letter = 'z'
if letter in guesses: # true if in guesses
    print(letter)
else: # false if not found in guesses
    print('- _ - ')

print()

name = "liz"
for char in name:
    print(char.upper()*3) 

print()

message = "Testing"
count = 0
for character in message:
 print(f'Index:{count}, Character:{character}')
 count += 1
