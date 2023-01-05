# Program that takes camel case input and outputs as snake case

# Define function that checks if a letter is capital
# if True lowercase it and precede with underscore

# User input
camelCase = input('camelCase: ')
# Empty string variable to add characters into
snakeCase = ""
# For loop to iterate over input
for c in camelCase:
    # Add _ + lowercase char if it is uppercase, else add char unchanged
    if c.isupper() == True:
      snakeCase +=  "_" + c.lower()
    else:
        snakeCase += c
# F string for clarity
print(f"Snake Case: {snakeCase}")



