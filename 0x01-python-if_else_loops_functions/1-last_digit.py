#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = -last

if last > 5:
    status = "and is greater than 5"
elif last == 0:
    status = "and is 0"
else:
    status = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last} {status}")
