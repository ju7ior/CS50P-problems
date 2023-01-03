#take users input and strip, then assign indexes to a variable, 
# define y as the function to run calculations

# Take input
xyz = input('Calculator input: ')

# Get numbers that will be used for calculations and remove white space for 
# more accuracy
x = float(xyz.replace(' ','')[0])
z = float(xyz.replace(' ','')[2])
# Get operator and remove white space
y = xyz.replace(' ','')[1]
# Define function that runs the mathematical operation
def operator(y):
    if y == '+' :
        result = x + z
    elif y == '-' :
       result = x - z
    elif y == '*' :
        result = x * z
    elif y == '/' :
        result = x / z
    else:
        result = 'Operator not valid(+,-,*,/)'
    return result
#print result
print(operator(y))

