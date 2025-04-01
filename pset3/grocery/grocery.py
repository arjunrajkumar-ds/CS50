# Program that prompts user for items, one per line, until CTRL-D
# Outputs the grocery list in uppercase and sorted alphabetically
# Should count how many times an item was input


# Function that adds an item that isn't currently in the dict
def new_item(str, dict):
    dict[str] = 1

# Function that increments the value of a key already stored
def existing_item(str, dict):
    dict[str] += 1

def add_item(str, dict):
    if str in dict:
        dict[str] += 1
    else:
        dict[str] = 1

def main():
    unsorted = {}
    while True:
        # Block of code that handles adding/updating items in unsorted
        try:
            item = input("").upper().strip()
            if item == '':
                continue
            add_item(item, unsorted)
        except (EOFError, KeyboardInterrupt):
            break

    # Block of code that renders output
    alpha_sorted = sorted(unsorted)
    print("\n")
    for i in alpha_sorted:
        print(f"{unsorted[i]} {i}")

main()

