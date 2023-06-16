minutes = eval(input("Enter the number of minutes: "))

years = minutes // (365 * 24 * 60)
days = (minutes % (365 * 24 * 60)) // (60 * 24)

print(minutes, "minutes is approximately", years, "years and", days, "days.")
