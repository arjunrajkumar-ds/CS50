# Program that simulates 'little professor' - a maths game
# Generates 10 different math problems to be solved by user
    # Incorrect guess -> 'EEE'
    # After 3 incorrect guesses, correct answer is displayed
# Prompts user for level; 1, 2, 3 - dictates how many digits
# Generates 10 X + Y problems 

import random
import sys

def main():
    level = get_level()
    i = 0
    score = 0
    while True and i < 10:
        try:
            X, Y = generate_integer(level)
            guess = -1
            sum = X + Y
            err_count = 0
            while guess != sum and err_count < 3:
                try:
                    print(f"{X} + {Y} = ", end = '')
                    guess = int(input(""))
                    if guess != sum and err_count < 3:
                        print("EEE")
                        err_count += 1
                    elif guess != sum and err_count == 3:
                        print(f"{X} + {Y} = {sum}\n", end = '')
                        break
                    elif guess == sum:
                        i += 1
                        score += 1
                        break
                except ValueError:
                    print("EEE")
                    err_count += 1
                    if err_count == 3:
                        print(sum)
                        break
                    continue
        except (KeyboardInterrupt, EOFError):
            sys.exit(0)
            break
        finally:
            if i == 10:
                print(f"Score: {score}")
                sys.exit(0)

                
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
        return random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999), random.randint(100, 999)
    
if __name__ == "__main__":
    main()