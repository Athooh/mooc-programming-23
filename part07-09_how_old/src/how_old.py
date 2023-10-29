# Write your solution here
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

year_of_birth = datetime(year, month, day)
millenium = datetime(1999, 12, 31)

if millenium > year_of_birth:
    days_diff = millenium - year_of_birth
    print(f"You were {days_diff.days} days old on the eve of the new millenium.")
else:
    print("You weren't born yet on the eve of the new millenium.")

# from datetime import datetime

# day = int(input("Day: "))
# month = int(input("Month: "))
# year = int(input("Year: "))

# def is_leap_year(year):
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         return True
#     return False

# def days_in_month(month, year):
#     if month in [4, 6, 9, 11]:
#         return 30
#     elif month == 2:
#         return 29 if is_leap_year(year) else 28
#     else:
#         return 31

# def days_until_new_millennium(day, month, year):
#     days = 0
#     while year < 2000 or (year == 2000 and month < 12):
#         days += days_in_month(month, year) - day + 1
#         day = 1
#         month += 1
#         if month > 12:
#             month = 1
#             year += 1
#     return days - 1  # Subtract 1 to exclude the eve of the new millennium

# year_of_birth = datetime(year, month, day)
# millennium = datetime(1999, 12, 31)

# days_old = days_until_new_millennium(day, month, year)

# if days_old >= 0:
#     print(f"You were {days_old} days old on the eve of the new millennium.")
# else:
#     print("You weren't born yet on the eve of the new millennium.")
