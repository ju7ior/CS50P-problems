# Create dict to store results
groceries = {}

# Infinite loop so user must exit out of loop with control d
while True:
    try:
        # Ask for input
        item = input("").lower().strip()
        # Check if item is in dict, if yes add 1 if not add to dict
        if item in groceries:
            groceries[item] += 1
       # if it is add 1 to the count
        else:
            groceries[item] = 1
    # If control d print itema and exit loop
    except EOFError:
        # Print sorted items with number
        for key in sorted(groceries.keys()):
            print(groceries[key], key)
        break