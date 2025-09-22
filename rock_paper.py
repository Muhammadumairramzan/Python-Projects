import random

choices = ['r', 'p', 's']

print("Welcome to Rock-Paper-Scissors!")
print("r = Rock, p = Paper, s = Scissors")

user_choice = input("Choose (r/p/s): ").lower()

if user_choice not in choices:
    print("Invalid choice! Please choose r, p, or s.")
else:

    computer_choice = random.choice(choices)


    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")


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
