def reverse(number):
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number //= 10
    return reversed_number

integer = eval(input("Enter an integer: "))
reversed_integer = reverse(integer)
print("Reversed integer:", reversed_integer)
