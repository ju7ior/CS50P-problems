# Ask user for input and if the input is 42 or case insensitively forty two
# or forty-two print yes, otherwise print no

# Take input
ans = input('What is the Answer to the Great Question of Life, the Universe, and Everything?: ')
# Lower input to make case insenstive
answer = ans.lower()
# Match answer 
match answer:
    case 'forty two' | 'forty-two' | '42':
        print('Yes.')
    case _:
        print('No.')
