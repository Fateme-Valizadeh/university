month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))

days_in_month = {
    1: 31,  # January
    2: 28,  # February (default, assuming it's not a leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31  # December
}

if month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    days_in_month[2] = 29

month_name = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
print(month_name[month - 1], year, "has", days_in_month[month], "days.")
