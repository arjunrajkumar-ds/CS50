# Program that removes vowels from a word
# Maintains capital letters

'''
Twitter -> Twttr
What's your name -> Wht's yr nm?
CS50 -> CS50
'''

# Pseudocode:
# Takes input and iterate over each letter
# If a vowel is detected, replace with ""

def shorten(word):
    shortened = ''
    for letter in word:
        if letter.upper() not in ['A', 'E', 'I', 'O', 'U'] and letter.isalpha():
            shortened = shortened + letter

    return shortened

def main():
    phrase = input("Input: ")
    word = shorten(phrase)
    print(word)

if __name__ == '__main__':
    main()