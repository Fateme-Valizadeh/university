def decimal_to_binary():
    decimal = eval(input("Enter a decimal integer: "))
    binary = bin(decimal)[2:]  
    print("Binary representation:", binary)


decimal_to_binary()
