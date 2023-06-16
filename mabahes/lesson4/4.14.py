import random

coin_flip = random.randint(0, 1)

user_guess = int(input("Guess the coin flip (0 for head, 1 for tail): "))

outcomes = ["head", "tail"]

if user_guess == coin_flip:
    print("Congratulations! It's", outcomes[coin_flip] + ". You guessed correctly!")
else:
    print("Sorry, it's", outcomes[coin_flip] + ". You guessed incorrectly.")