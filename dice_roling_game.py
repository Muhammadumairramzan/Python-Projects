import random

playing = True
while playing:
    choice = input("Roll THE DICE? (Y/N): ").lower()
    if choice == "y":
        dial1 = random.randint(1,6)
        # dial2 = random.randint(1,6)
        print(f"{dial1}")
    elif choice == "n":
        print("thanks for playing")
        break
    else:
        print("Invalid choice")
