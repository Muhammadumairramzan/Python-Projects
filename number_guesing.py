import random

number_to_guess = random.randint(1,100)
while True:

    try:
        user = int(input('guss number b/w 1-100: '))
        if user > number_to_guess:
            print("too low")
        elif user < number_to_guess:
            print("too high")
        else:
            print("done")
            break
    except ValueError:
        print("Invalid operation")