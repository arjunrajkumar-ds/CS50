# Program that takes an input and converts string representations to smiley/sad faces

def main():
    string = input()
    print(convert(string))

def convert(emote):
    emote = emote.replace(":)", "🙂")
    emote = emote.replace(":(", "🙁")
    return emote

main()