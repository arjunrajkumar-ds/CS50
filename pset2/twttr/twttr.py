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

def main():
    phrase = input("Input: ")
    corrected = []
    for letter in phrase:
        if letter.upper() not in ['A', 'E', 'I', 'O', 'U']:
            corrected.append(letter)
    for letter in corrected:
        print(letter, sep="", end="")

main()