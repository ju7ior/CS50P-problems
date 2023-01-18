#In a file called fuel.py, implement a program that prompts the user for a fraction,
#formatted as X/Y, wherein each of X and Y is an integer, and then outputs,
#as a percentage rounded to the nearest integer, how much fuel is in the tank.
#If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
#And if 99% or more remains, output F instead to indicate that the tank is essentially full.
def main():
    # Call getPercent function and calculate what the output should be
    pct = getPercent()
    if pct <= 1:
        print("E")
    elif pct >= 99:
        print("F")
    else:
        print(f"{pct}%")


def getPercent():
    while True:
        try:
            # Ask user for fraction
            fraction = input("Fraction:(x/y) ")
            # Turn fraction input to integers so it can be used in calculations
            x, y = fraction.split('/')
            x, y = int(x), int(y)
            if x > y:
                continue
            result = x / y
            pct = result * 100

            return int(pct)
        except ValueError:
            pass
        except ZeroDivisionError:
            print("Can't divide by Zero.")

main()
