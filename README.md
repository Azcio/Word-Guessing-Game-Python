# Word-Guessing-Game-Python
This project is a Python-based word guessing game where players try to uncover a random word between 5–10 letters. It includes both a terminal version and a Tkinter-powered GUI inspired by Wordle.
The game challenges players to guess the correct word within limited attempts, highlighting letters as:

Green → Correct letter, correct position
Yellow → Letter exists in word, wrong position
Gray → Letter not in word

Features
Random word selection from a filtered dictionary file.
Terminal version: classic hangman-style word guessing.
GUI version: Wordle-style grid built with Tkinter.
Live feedback on guesses with colors.
Smooth fade-in win/lose messages.
Clear win and lose conditions

Run in the Terminal:
python src/app.py

Run with the GUI
python -m gui.gui

Skills & Technologies Used

Python: core language.
Tkinter: built the GUI interface.
Game Logic: win/lose conditions, input validation, state management.
Problem Solving: designed algorithms for comparing guesses to the answer.
File Handling: loading filtered words from a text file.
Clean Code Practices: meaningful variable names, modular functions.
