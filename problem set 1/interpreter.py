#take users input and strip, then assign indexes to a variable, 
# define y as the function to run calculations

xyz = input('Calculator input: x')

# get numbers that will be used for calculations
x = float(xyz.replace(' ','')[0])
z = float(xyz.replace(' ','')[2])
#get operator
y = xyz.replace(' ','')[1]

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

print(operator(y))

