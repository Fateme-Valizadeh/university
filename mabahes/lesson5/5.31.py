import calendar

def display_calendar():
    year = int(input("Enter the year: "))
    first_day = int(input("Enter the first day of the year (0 for Monday, 1 for Tuesday, and so on): "))

    for month in range(1, 13):

        cal = calendar.monthcalendar(year, month)

        month_name = calendar.month_name[month]

        print(f"\n{month_name} {year}")

        print("Mon Tue Wed Thu Fri Sat Sun")

        starting_day = (first_day + 1) % 7

        for week in cal:
            line = ""
            for day in week:
                if day == 0:
                    line += "    "
                else:
                    line += f"{day:3d} "
            print(line)

        first_day = (first_day + calendar.monthrange(year, month)[1]) % 7


display_calendar()
