positive_count = 0
negative_count = 0
total = 0
count = 0

while True:
    number = int(input("Enter an integer (0 to end): "))
    
    if number == 0:
        break
        
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
        
    total += number
    count += 1

if count > 0:
    average = total / count
    print("Positive numbers count:", positive_count)
    print("Negative numbers count:", negative_count)
    print("Total:", total)
    print("Average:", average)
else:
    print("No numbers were entered.")