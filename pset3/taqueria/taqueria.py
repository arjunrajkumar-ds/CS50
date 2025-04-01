# A program that allows a user to place an order - prompting for items
# until CTRL-D. After each inputted item (each on a new line),
# display the total cost of items so far to 2 decimals

products = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    sum = 0
    while True:
        try:
            order = input("Item: ").title()
            if order == '':
                continue
            if order not in products:
                continue
            sum += products.get(order,0)
        except (EOFError, KeyboardInterrupt):
            break
        print(f"Total: ${sum:.2f}")

main()