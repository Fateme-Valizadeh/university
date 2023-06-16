def sumDigits(n):
    total = 0
    while n != 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

integer = int(input("Enter an integer: "))
result = sumDigits(integer)
print("Sum of digits:", result)
