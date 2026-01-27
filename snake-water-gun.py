import random

# s = snake, w = water, g = gun
choices = ['s', 'w', 'g']

# Take input from user
player = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Validate input
if player not in choices:
    print("Invalid input! Please choose s, w, or g.")
else:
    # Computer choice
    computer = random.choice(choices)

    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a Tie!")
        print("No points awarded.")

    elif player == 's':
        if computer == 'w':
            print("You win! 🐍 drinks 💧")
        else:
            print("Computer wins! 🔫 kills 🐍")

    elif player == 'w':
        if computer == 'g':
            print("You win! 💧 destroys 🔫")
        else:
            print("Computer wins! 🐍 drinks 💧")

    elif player == 'g':
        if computer == 's':
            print("You win! 🔫 kills 🐍")
        else:
            print("Computer wins! 💧 destroys 🔫")
