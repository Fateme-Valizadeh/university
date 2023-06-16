import math

length = eval(input("Enter the  length : "))

s = 2 * length * math.sin(3.1415/5)

Area = (3 * math.sqrt(3) / 2) * s**2 

print("The area of the pentagon is",int(Area*100)/100)