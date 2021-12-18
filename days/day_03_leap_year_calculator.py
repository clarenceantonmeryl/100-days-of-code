# year_input = int(input("What year do you want to check? "))


def is_leap(year):
    """Returns True if the 'year' is a leap year or returns False if the 'year' is not a leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month - 1]


print(days_in_month(2002, 2))


"""

if is_leap(year=year_input):
    print(f"The year {year_input} is a leap year.")
else:
    print(f"The year {year_input} is not a leap year.")
"""
