def main():
    greeting = input("Greeting: ").lstrip().lower()
    money = value(greeting)
    print(f"${money}")

def value(greeting):
    normalised = greeting.lstrip().lower()
    if normalised.startswith("hello"):
        return 0
    elif normalised[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()