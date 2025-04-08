# Program that simulates 'little professor' - a maths game
# Generates 10 different math problems to be solved by user
    # Incorrect guess -> 'EEE'
    # After 3 incorrect guesses, correct answer is displayed
# Prompts user for level; 1, 2, 3 - dictates how many digits
# Generates 10 X + Y problems 

import random

def main():
    while True:
        level = get_level()
        i = 1
        while i < 10:
            X, Y = generate_integer(level)
            guess = -1
            sum = X + Y
            count = 0
            while guess != sum:
                print(f"{X} + {Y} = ", end = '')
                guess = input("")
                if not guess.isnumeric:
                    continue
                elif guess != sum and count < 4:
                    print("EEE")
                    count += 1
                elif count == 3:
                    print(sum, end = '')
                    break
                elif guess == sum:
                    break
            i += 1

                


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(0, 99), random.randint(0, 99)
    elif level == 3:
        return random.randint(0, 999), random.randint(0, 999)
    
if __name__ == "__main__":
    main()