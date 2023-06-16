import random

num1 = random.randint(0, 99)
num2 = random.randint(0, 99)

answer = eval(input(f"What is {num1} * {num2}? "))

correct_answer = num1 * num2

if answer == correct_answer:
    print("Correct!")
else:
    print("Incorrect. The correct answer is", correct_answer)
