# Program that slows down 'speech', by adding an ellipsis in between
# Takes 3 words as input

def main():
    words = input()
    words = words.replace(" ", "...")
    print(words)

main()