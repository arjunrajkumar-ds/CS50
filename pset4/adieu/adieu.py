def main():
    names = []
    while True:
        try: 
            names.append(input("Name: ").title())
        except EOFError:
            print("\n")
            break
    
    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    elif len(names) > 2:
        print("Adieu, adieu, to ", end = '')
        for i in range(len(names) - 1):
            print(f"{names[i]}, ", end = '', sep = '')
        print(f"and {names[-1]}")
            
if __name__ == "__main__":
    main()