count = 0
for num in range(100, 201):
    if (num % 5 == 0 or num % 6 == 0) and not (num % 5 == 0 and num % 6 == 0):
        print(num, end=" ")
        count += 1
        if count % 10 == 0:
            print()  
if count % 10 != 0:
    print()
