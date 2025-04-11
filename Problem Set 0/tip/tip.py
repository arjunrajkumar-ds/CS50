def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What % would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Function that takes str input '$xx.yy' & returns the amount as a float
def dollars_to_float(d):
    amount = d[1:]
    return float(amount)

# Function that takes str input 'xx%' & returns the percentage as a float
def percent_to_float(p):
    percent = p[0:-1]
    return float(percent) / 100

main()