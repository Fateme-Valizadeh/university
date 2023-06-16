a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

determinant = a * d - b * c
if determinant == 0:
    print("The system of equations has no solution.")
else:
    x = (e * d - b * f) / determinant
    y = (a * f - e * c) / determinant

    print(" x is:", x ," y is:", y)
    
