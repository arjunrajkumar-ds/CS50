# Program that uses CoinCap API to give the user current price of x BTC
# API - https://rest.coincap.io/v3/assets/bitcoin?apiKey=92cf5d5014de41b0b47a8fec15789ba9c1f94bbdd7c6225dd1021646bb5e1c24

import requests
import sys

def retrieve_btc():
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=92cf5d5014de41b0b47a8fec15789ba9c1f94bbdd7c6225dd1021646bb5e1c24").json()
        price = response["data"]["priceUsd"]
    except requests.RequestException:
        print("Request exception - Probably API key wrong")
        sys.exit(0)
    return price

def main():
    try:
        if len(sys.argv) != 2:
            print("Missing command-line argument")
            sys.exit(1)
        if not sys.argv[1].isnumeric:
            print("Command-line argument is not a number")
            sys.exit(1)
        else:
            quantity = float(sys.argv[1])
    except IndexError:
        print("Missing command-line argument")
        sys.exit(1)
    price = float(retrieve_btc())
    value = round(price * quantity, 4)
    print(f"${format(value, ",")}", end = '')

if __name__ == "__main__":
    main()