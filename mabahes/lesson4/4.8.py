num1,num2,num3 = eval(input("Enter the first integer: "))

minimum = min(num1, num2, num3)
maximum = max(num1, num2, num3)
middle = (num1 + num2 + num3) - minimum - maximum

print("The integers in increasing order are:", minimum, middle, maximum)
