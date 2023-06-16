decimal_int = int(input("Enter an integer between 0 and 15: "))

hex_num = hex(decimal_int)[2:]

print("The hexadecimal equivalent of", decimal_int, "is", hex_num.upper())
