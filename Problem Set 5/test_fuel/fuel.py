# Program that prompts user for a fraction; x / y (int)
# Outputs the percentage representation of the fraction, rounded to nearest integer
# 1% or less -> E, 99% or more -> F

import sys

def main():
    while True:
        fraction = input("Fraction: ").strip()
        if valid_input(fraction):
            try:
                x, y = fraction.split("/")
                value = convert(x, y)
                gauge(value)
            except (ValueError, UnboundLocalError, ZeroDivisionError, TypeError):
                pass

# Checks input to confirm that it's valid
# Returns True / False
def valid_input(s):
    try:
        x, y = s.split("/")
    except (ValueError, TypeError, UnboundLocalError):
        return False
    if not float(x).is_integer or not float(y).is_integer():
        return False
    elif int(x) > int(y):
        return False
    else:
        return True

# Takes a string like 'X/Y' & returns the fraction as a percentage rounded to nearest number
def convert(n, m):
    try:
        quotient = float(n) / float(m) * 100
        if m == 0:
            raise ZeroDivisionError
        return int(round(quotient))
    except (ValueError):
        print("No values entered")

# Takes an integer and returns corresponding output string
def gauge(percentage):
    if percentage >= 99:
        print("F")
        sys.exit()
    elif percentage <= 1:
        print("E")
        sys.exit()
    else:
        print(f"{percentage}%")
        sys.exit()

if __name__ == "__main__":
    main()