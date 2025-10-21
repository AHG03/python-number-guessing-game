# Number Guessing Game 🔢

A simple, classic number guessing game implemented in Python. The computer selects a random number, and the player tries to guess it within the specified range.

---

## 🚀 Getting Started

### Prerequisites

You'll need Python 3 installed on your system to run this game.

### How to Run

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you saved number_guessing_game.py.
3.  Run the game using the Python interpreter:

   
    python number_guessing_game.py
    
---

## 🎮 How to Play

The goal is to guess the randomly selected number between 1 and 100.

1.  When prompted, enter your guess and press Enter.
2.  The game will provide hints to guide your next guess:
    * "Too low!"
    * "Too high!"
3.  The game ends when you successfully guess the number, displaying a "Congratulations!" message.
4.  If you enter non-numeric input (like text), the game will prompt you again with "Please enter a valid number."

---

## 💻 Code Overview

The script relies on a single file, number_guessing_game.py, and uses the following key Python concepts:

* **import random**: Used to generate the secret number.
* **random.randint(1, 100)**: Sets the range for the secret number.
* **while True:**: Creates an infinite loop that runs until the correct guess is made.
* **try...except ValueError**: Robust error handling to prevent crashes from non-numeric user input.
