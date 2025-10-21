# Number-guessing-game
🎯 Number Guesser (Python)

A simple but fun console-based number guessing game — except this time, the computer tries to guess your number using logic and binary search!

🧠 How It Works

This program flips the classic number guessing game:

You secretly think of a number.

The computer uses binary search to narrow it down until it finds the exact answer.

It tracks how many guesses it takes and celebrates when it wins.

It’s a great example of applying algorithms (binary search) and input validation in a Python console project.

⚙️ Features

✅ Input validation for all prompts
✅ Customizable guessing range
✅ Binary search algorithm for efficient guessing
✅ ASCII art intro for a polished look
✅ Attempts counter
✅ Clean and simple structure using functions

🧩 Code Structure
guess_number(min_input, max_input) → Handles the guessing logic  
start_game() → Welcomes the player and confirms readiness  
get_range() → Asks user for min and max limits with validation  
main() → Runs the program flow and displays banner art

🚀 How to Run

Make sure you have Python 3.x installed.

Clone or download this repository.

Open a terminal in the project folder.

Run the program:

python number_guesser.py


Follow the prompts:

Think of a number

Enter a valid range

Tell the program if its guess is higher, lower, or correct

💡 Example Gameplay
Welcome to the number guesser, have you thought of a number yet? (y)/(n): y
Give me a minimum value to go down to: 1
Give me a maximum value to go up to: 100
Is your number.. 50? (y)(n): n
Higher or lower? (h)/(l): h
Is your number.. 75? (y)(n): y
YESSS! I guessed it! I win! Thanks for playing!
I guessed the number in: 2 tries O _ O

🧰 Skills Demonstrated

Python functions and modular structure

Error handling and input validation

Binary search logic

Console interaction design

🏷️ Author

Created by pheebee14
A small but logical step toward building smarter interactive programs.

License: MIT — feel free to use, modify, and learn from this project!
