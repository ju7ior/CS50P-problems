# Program that asks user for 50 cents, accepts 25, 10 and 5 cents
# until user has inputted at least 50 cents, if they are owed change print change

# Assign cost outside function and print amount due
cost = 50
print(f"Amount due: {cost}¢")

def main(cost):
    # Ask for input while there is an amount due
    while cost > 0:
        coin = int(input("Insert Coin(25, 10, 5): "))
        # If coin is not accepted ignore input
        if coin not in [25,10,5]:
            continue 
        cost -= coin
        # If amount is due print it
        if cost > 0:
            print(f"Amount due: {cost}¢")
    # If no change is owed print purchase statement
    if cost == 0:
        print("Heres your coke!")
    # If change is owed print how much change is owed and also print purchase statement
    else:
        print(f"Change owed: {-cost}¢\nHeres your Coke!")
    return
# Run function with costs
main(cost)