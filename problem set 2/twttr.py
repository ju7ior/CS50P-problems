# Make a program that removes vowels from user input regardless of case

# Ask for input and assign variables that will be used
string = input('Input: ')
vowels = ['A','a','E','e','I','i','O','o','U','u']
newString = ''
# For loop to only add letters not in vowels list to new String
for s in string:
    if s not in vowels:
        newString += str(s)
# Output new string
print(f'Output: {newString}')