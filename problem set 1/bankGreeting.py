# Prompt the user for input, if user inputs hello print $0
# If user input starts with a h print $20
# if user input is not Hello  and doesn't  with a H print $100

# Define main function
def main(greeting):
    greeting.lower()
    if greeting.startswith('hello'):
        print('$0')
    elif greeting.startswith('h'): 
        print('$20')
    else:
        print('$100')

greeting = input('Greet customer: ')
main(greeting)