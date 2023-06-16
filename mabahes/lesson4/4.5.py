today = int(input("Enter today's day: "))
days_after = int(input("Enter the number of days elapsed since today :"))

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

future_day = (today + days_after) % 7

print("The future day is", days_of_week[future_day])
