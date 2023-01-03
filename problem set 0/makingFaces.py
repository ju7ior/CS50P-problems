# Convert emoticons in input to emojis

# Take input 
string = str(input("Input Text: "))
# Define function that converts emoticons to emojis
def emojifier(string):
    return string.replace(":)", "🙂").replace(":(", "🙁")
# Call the function and print the result
print(emojifier(string))