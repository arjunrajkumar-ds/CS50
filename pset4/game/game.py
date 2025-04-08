# Program that simulates a guessing game
# Player enters the level they'd like to play, [1,100]
    # If not a positive integer, try again
# Randomly generates an integer between 1, n
# Prompts the user to guess the number
    # Gives too low, too high hints after each guess

import random
import sys


def input_validator(n):
    if type(n) == int and 0 <= n <= 100:
        return True
    else:
        return False

def main():
    while True:
        try:
            level = int(input("Level: "))
            if not input_validator(level):
                pass
            else:
                rng = random.randint(0, level)
                guess = -1
                while guess != rng:
                    guess = int(input("Guess: "))
                    if not input_validator(guess):
                        continue
                    elif guess < 0:
                        continue
                    else:
                        if guess < rng:
                            print("Too small!")
                            continue
                        elif guess > rng:
                            print("Too large!")
                            continue
                        elif guess == rng:
                            print("Just right!")
                            guess = rng
                            sys.exit(1)
        except (EOFError, KeyboardInterrupt):
            break
        except ValueError:
            continue




if __name__ == "__main__":
    main()