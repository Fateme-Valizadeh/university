final_value = eval(input("Enter the final account value: "))
interest_rate = eval(input("Enter annual interest rate in percent: "))
years = eval(input("Enter the number of years: "))

interest_rate /= 100
month = 12
initial_deposit =  final_value / ((1 + (interest_rate / month))**(month*years))
print("The initial deposit value is:", initial_deposit)