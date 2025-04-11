# Program that uses the emoji package to convert strings to emojis

import emoji

#print(emoji.emojize("Python is :thumbs_up:"))

def validate_input(str):
    pass

def main():
    input_string = input("Input: ")

    emojized = emoji.emojize(input_string)
    print("Output:", emojized)

if __name__ == "__main__":
    main()