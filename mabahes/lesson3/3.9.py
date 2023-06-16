name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked in a week: "))
hourly_rate = float(input("Enter hourly pay rate: "))
federal_tax_rate = float(input("Enter federal tax withholding rate (%): ")) / 100
state_tax_rate = float(input("Enter state tax withholding rate (%): ")) / 100


gross_pay = hours_worked * hourly_rate

federal_withholding = gross_pay * federal_tax_rate

state_withholding = gross_pay * state_tax_rate

total_withholding = (federal_withholding*100) + (state_withholding*100)

net_pay = gross_pay-total_withholding

print("Deductions :\n ")
print("Payroll statement for", name)
print("Hours worked:", hours_worked)
print("Hourly pay rate: $", hourly_rate )
print("Gross pay: $", gross_pay)
print("Federal withholding amount: $",federal_withholding )
print("State withholding amount: $", state_withholding)
print("Total withholding amount: $", total_withholding)
print("Net pay: $", net_pay)

