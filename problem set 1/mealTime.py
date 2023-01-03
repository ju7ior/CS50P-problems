# Program that tells if it is time to eat a meal 
# according to what time the user inputs (##:## format expected)
def main():
    time = input('What is the time?: ')
    converted = convert(time)
    if converted >= 8.0 and converted <= 9.0:
        print('Breakfast time.')
    if converted >= 12.0 and converted <= 13.0:
        print('Lunch time.')
    if converted >= 18.0 and converted <= 19.0:
        print('Dinner time.')
    else:
        print("It isn't time to eat.")
# Define function that converts time from the user format
# into a float for comparison operations
def convert(time):
    hour, minute =  (time.split(':'))
    minutes = float(minute) / 60
    return float(hour) + minutes
# Run function
if __name__ == "__main__":
    main()
