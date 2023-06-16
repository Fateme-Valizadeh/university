import time
import random

current_time = int(time.time())

random.seed(current_time)

random_letter = chr(random.randint(65, 90))

print("Random uppercase letter:", random_letter)
