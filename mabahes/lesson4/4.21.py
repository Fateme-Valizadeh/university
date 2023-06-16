year = int(input("Enter the year : "))
month = int(input("Enter the month : "))
day = int(input("Enter the day of the month : "))


if month == 1 or month == 2:
    month += 12
    year -= 1


h = (day + (13*(month+1)//5) + year + (year//4) - (year//100) + (year//400)) % 7

days_of_week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day_of_week = days_of_week[h]


print("The day of the week for", month, "/", day, "/", year, "is", day_of_week + ".")
