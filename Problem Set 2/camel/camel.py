# Program that takes input for the name of a variable in camel case & outputs the corresponding name in snake case

def main():
    variable = input("camelCase: ")
    for letter in variable:
        if letter.islower():
            print(letter, end="")
        else:
            print('_'+letter.lower(), end="")
main()