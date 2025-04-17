# Already abstracted it in Week 2 - no extra work required

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if two_letters(s) and char_limit(s) and special_char(s) and middle_number(s):
        return True
    else:
        return False

# Function to check that first two letters are letters
def two_letters(s):
    return s[0:2].isalpha()

# Function to check that char limit is followed
def char_limit(s):
    return (len(s) >= 2 and len(s) <= 6)

# Function to check that no special characters in string
def special_char(s):
    invalid = [" ", ".", "!", ",", ".", "_", "&"]
    check = 1
    for letter in s:
        if letter in invalid:
            check -= 1
    if check>0:
        return True
    else:
        return False

# Function to check that numbers are not in the middle - only at the end, and first number isnt 0
def middle_number(s):
    if s.isalpha():
        return True
    
    substring = ""
    for letter in range(len(s)):
        if not s[letter].isalpha():
            substring = s[letter:]
            break
    if substring.isnumeric() and substring[0] != '0':
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()