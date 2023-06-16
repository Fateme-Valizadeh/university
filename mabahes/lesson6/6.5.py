def displaySortedNumbers(num1, num2, num3):
    sorted_numbers = sorted([num1, num2, num3])
    for num in sorted_numbers:
        print(num, end=' ')

# Test program
num1,num2,num3 = eval(input("Enter the first number: "))

print("Numbers in increasing order:")
displaySortedNumbers(num1, num2, num3)
