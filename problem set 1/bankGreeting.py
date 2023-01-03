# Prompt the user for input, if user inputs hello print $0
# If user input starts with a h print $20
# if user input is not Hello  and doesn't  with a H print $100

def main(greeting):
    if greeting[0:5].lower() == 'hello':
        print('$0')
    elif greeting[0].lower() == 'h' : 
        print('$20')
    else:
        print('$100')

greeting = input('Greet customer: ')
main(greeting)