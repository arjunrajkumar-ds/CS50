# Program that prompts user for a fraction; x / y (int)
# Outputs the percentage representation of the fraction, rounded to nearest integer
# 1% or less -> E, 99% or more -> F

def main():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            x, y = fraction.split("/")
            fraction = float(x) / float(y) * 100
        except (ValueError, UnboundLocalError, ZeroDivisionError, TypeError):
            pass
        else:
            if not float(x).is_integer() or not float(y).is_integer():
                continue
            elif int(x) > int(y):
                continue
            elif fraction >= 99:
                print("F")
                break
            elif fraction <= 1:
                print("E")
                break
            else:
                print(f"{round(fraction)}%")
                break
    
                
    

main()