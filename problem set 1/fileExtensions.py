# Program that outputs a different reply depending on the suffix    
# of the file name the user inputs, must be case insensitive.

# Get file name and make it case insensitive
file = input('File name: ').lower()
# Define function that matches file suffix
# and prints the matching prompt.
def fileSuffix(file):
    if file.endswith('.jpeg') or file.endswith('.jpg'):
        print('image/jpeg')
    elif file.endswith('.gif'):
        print('image/gif')
    elif file.endswith('.png'):
        print('image/png')
    elif file.endswith('.pdf'):
        print('application/pdf')
    elif file.endswith('.txt'):
        print('text/plain')
    elif file.endswith('.zip'):
        print('application/zip')
    else:
        print('application/octet-stream')
        
 # Call function with input   
fileSuffix(file)
