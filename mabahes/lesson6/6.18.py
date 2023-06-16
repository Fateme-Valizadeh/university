import random

def printMatrix(n):
    for i in range(n):
        for j in range(n):
            element = random.randint(0, 1)
            print(element, end=' ')
        print()

n = int(input("Enter the value of n: "))
print("Matrix:")
printMatrix(n)
