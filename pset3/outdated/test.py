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
    
def main():
    input_string = input("Date: ")
    print(is_valid_date(input_string))

main()