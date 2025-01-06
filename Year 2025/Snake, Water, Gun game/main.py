import random

running = True
while running:
    comp = random.choice([1,2,3])
    print("Enter 1 for snake")
    print("Enter 2 for water")
    print("Enter 3 for gun")
    print("Enter 8 to quit")
    user = int(input("Please enter your choice: "))
    if user == 8:
        running = False
        break
    if not user in [1,2,3]:
        raise ValueError
    value = ["CorrectingIndex", "snake", "water", "gun"]
    print(f"Thanks for chosing you have chosen {value[user]}")
    print(f"Computer has chosen {value[comp]}")
    user = value[user]
    comp = value[comp]
    if user == comp:
        print("It's a draw")
    elif user == 'snake' and comp == 'water':
        print("You win!")
    elif user == 'snake' and comp == 'gun':
        print("You lost :(")
        
    elif user == 'water' and comp == 'gun':
        print("You win!")
    elif user == 'water' and comp == 'snake':
        print("You lost :(")
        
    elif user == 'gun' and comp == 'snake':
        print("You win!")
    elif user == 'gun' and comp == 'water':
        print("You lost :(")
print("Thanks for playing")