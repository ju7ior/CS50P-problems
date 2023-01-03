# Take mass input and use it to calculate E = mc^2

# Take input as int
mass = int(input("Mass(kg): "))
# Define formula function
def formula(mass):
    E = mass * pow(300000000, 2)
    return E
# Call function and store value
result = formula(mass)
# Print result with commas
print(f"{result: ,}")