import random

random_value = random.randint(1, 100)
while True:
    try:
        choice = int(input("Guess the number between 1 and 100: "))
        if choice < random_value:
            print("Too low!")
        elif choice > random_value:
            print("Too high!")
        elif choice == random_value:
            print("Congradulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number.")