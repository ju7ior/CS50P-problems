# Create menu dict with value
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# Create total that will be displayed
total = 0
# Infinite loop so user must break it 
while True:
    try:
        food = input('Item: ')
        if food in menu:
            # Add keys value to total and display new total
            total += menu[food]
            print(f"Total: {total}$")
    except EOFError:
        print("\n Thanks.")
        break
            
