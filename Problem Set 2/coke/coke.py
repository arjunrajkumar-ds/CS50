# Vending machine sells coke for 50c
# Only accepts coins of denomination 25, 10, 5
# Program that prompts user to enter coins, one at a time
# Provides updated balance after each insert & change at the end

def main():
    balance = 50
    while balance>0:
        print(f"Amount Due: {balance}")
        deposit = int(input("Insert Coin: "))
        if deposit in [5, 10, 25]:
            balance -= deposit
            if balance <= 0:
                print(f"Change Owed: {abs(balance)}")

main()