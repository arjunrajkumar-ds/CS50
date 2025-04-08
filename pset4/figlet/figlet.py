# Program that prompts user for a `str` of text & outputs it in the desired font
# Expects 0 or 2 command-line arguments
# - 0 for random font
# - 2 for '-f' or '--font' & <name_of_font>

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()


def font_validator(font):
    if font in fonts:
        return True

def main():
    try:
        if len(sys.argv) == 1:
            input_string = input("Input: ")
            rand = random.randint(1, len(fonts))
            figlet.setFont(font = fonts[rand])
        elif len(sys.argv) == 3:
            if sys.argv[1] not in ("-f", "--font"):
                print("Invalid usage")
                sys.exit(1)
            elif sys.argv[1] == "-f" or "--font" and font_validator(sys.argv[2]):
                figlet.setFont(font = sys.argv[2])
                input_string = input("Input: ")
        else:
            print("Invalid usage")
            sys.exit(1)
        print("Output: \n")
        print(figlet.renderText(input_string))
    except (IndexError, UnboundLocalError):
        print("Invalid usage")
        sys.exit(1)

    

if __name__ == "__main__":
    main()