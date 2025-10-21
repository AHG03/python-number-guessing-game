import random

choice = int(input("Guess the number between 1 and 100: ")
random_value = random.randint(1, 100)

while True:
    if choice < random_value:
        print("Too low!")
    elif choice > random_value:
        print("Too high!")
    elif choice == random_value:
        print("Congradulations! You guessed the number.")
        break
    else:
        print("Please enter a valid number.")