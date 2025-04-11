# Input is string ##:## 24H time
# Need to isolate and convert to float

def main():
    time = input("What time is it? ")
    converted = convert(time)
    if converted >= 7 and converted <= 8:
        print("breakfast time")
    elif converted >= 12 and converted <= 13:
        print("lunch time")
    elif converted >= 18 and converted <= 19:
        print("dinner time")
    else:
        pass


# Function to take 24H time str and output the time as a float
# e.g. 07:30 -> 7.5
def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute) / 60
    converted = hour+minute
    return converted

if __name__ == "__main__":
    main()