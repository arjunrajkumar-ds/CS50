# In the US, dates are typically formatted MM/DD/YYYY
# Computers use ISO8601 -> YYYY/MM/DD, padding with leading 0s as required
# This program prompts a user for a date in month-day-year and outputs the same in corrected format
# Assume that every month has 31 days

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def is_valid_date(str):
    try:
        # Case 1 - MM/DD/YYYY format
        if str.count('/') == 2 and ',' not in str:
            splits = str.split('/')
            if len(splits) != 3:
                return False
            else:
                month, day, year = splits

            # Check all inputs are digits
            if not (month.isdigit() and day.isdigit() and year.isdigit()):
                return False
            
            month = int(month)
            day = int(day)
            year = int(year)
            if not(1 <= month <= 12 and 1 <= day <= 31):
                return False
            
            return True
        
        # Case 2 - 'September 9, 1936' format
        elif str.count(',') == 1 and '/' not in str:
            splits = str.split(' ')
            if splits[1][-1] != ',' or len(splits) != 3:
                return False
            month_name, day, year = splits
            if month_name not in months:
                return False
            month = months.index(month_name)
            
            
            if not (1<= int(day[:-1]) <= 31) or not day[:-1].isdigit():
                return False
            day = int(day[:-1])
            
            if not year.isdigit():
                return False
            year = int(year)

            return True
    except (ValueError, IndexError):
        return False

# Function to check format. Doesn't need extra rules to validate
# since this will come afterwards 
# Returns 1 for 1st format, 2 for 2nd format
def check_format(str):
    if str.count('/') == 2:
        return 1
    elif ',' in str:
        return 2

def main():
    while True:
        input_string = input("Date: ").strip()
        if not is_valid_date(input_string):
            continue
        # Input is valid
        # Check which format
        check = check_format(input_string)
        if check == 1:
            # Case 1
            month, day, year = input_string.split('/')
            month = int(month)
            day = int(day)
            year = int(year)

            print(f"{year}-", end = '')
            print("{:02d}-".format(month), end = '')
            print("{:02d}".format(day))
            break
        elif check == 2:
            # Case 2
            month_name, day, year = input_string.split()
            month = months.index(month_name) + 1
            day = day[:-1]
            month = int(month)
            day = int(day)
            year = int(year)

            print(f"{year}-", end = '')
            print("{:02d}-".format(month), end = '')
            print("{:02d}".format(day))
            break

        

main()



# print("{:02d}".format(number))