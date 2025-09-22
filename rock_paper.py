import random

# Available choices
choices = ['r', 'p', 's']

print("Welcome to Rock-Paper-Scissors!")
print("r = Rock, p = Paper, s = Scissors")

# Get user choice
user_choice = input("Choose (r/p/s): ").lower()

# Validate input
if user_choice not in choices:
    print("Invalid choice! Please choose r, p, or s.")
else:
    # Computer choice
    computer_choice = random.choice(choices)

    # Show both choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')
    ):
        print("You win! 🎉")
    else:
        print("Computer wins! 🤖")
