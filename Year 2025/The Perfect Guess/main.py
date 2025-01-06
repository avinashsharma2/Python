import random

num = random.randint(0, 1000)
tries = 0
user_num = int(input("Guess a number between 0 and 1000: "))

while num != user_num:
    if num > user_num:
        print("Too small try something smaller")
        user_num = int(input("Guess a number here: "))
    elif num < user_num:
        print("Too big try something smaller")
        user_num = int(input("Guess a number here: "))
    tries += 1
    
print(f"Congrats for successfully guessing {num}")
print(f"You took {tries} tries")