# Finish writing functions for tip calculator

# Main function
def main():
    dollars = dollarsToFloat(input("How much was the meal? "))
    percent = percentToFloat(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollarsToFloat(d):
    # Strip dollar sign and return as float
    return float(d.strip('$'))


def percentToFloat(p):
    # Strip percent sign and return as float
    return float(p.strip('%')) / 100

# Run program
if __name__ == '__main__':
    main()