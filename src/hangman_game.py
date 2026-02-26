
# Libraries
import random
import tkinter as tk

from PIL import Image, ImageTk


# Read and execute manual setup
manual_content = open("manual.py", "r").read()
exec(manual_content)
show_manual("../data/hangman_manual.md")

# Read word categories
manual_content = open("word_categories.py", "r").read()
exec(manual_content)

categories = {
    "Food": food,
    "Feelings": feelings,
    "Countries": countries,
    "Names": names,
    "Things": things,
    "Animals": animals,
    "Artists": artists
}


# Game mechanics
def show_hangman():
    """Display hangman image window."""
    window = tk.Tk()
    window.title("Hangman")
    window.resizable(False, False)

    image_path = Image.open("../IMG/Hangman.ico")
    photo = ImageTk.PhotoImage(image_path)

    label = tk.Label(window, image=photo)
    label.pack()
    window.mainloop()


def select_word():
    """Select random word from user-chosen category."""
    try:
        category = input(
            "Enter category (Food, Feelings, Countries, Names, Things, Animals, Artists): "
        ).capitalize()

        print(f"Category: {category}")
        word = random.choice(categories[category])
        return word

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def initialize_board(word):
    """Create empty board with underscores."""
    return ["_"] * len(word)


def display_board(board):
    """Print current board state."""
    print(" ".join(board))


def ask_letter():
    """Get letter input from user."""
    try:
        letter = input("Enter a letter: ")
        return letter.lower()

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def update_board(word, board, letter):
    """Update board with correctly guessed letter."""
    for i in range(len(word)):
        if word[i] == letter:
            board[i] = letter


def play_hangman():
    """Main game loop."""
    word = select_word()
    if not word:
        return

    max_attempts = 6
    attempts = 0
    board = initialize_board(word)

    try:
        while "_" in board and attempts < max_attempts:
            display_board(board)
            letter = ask_letter()

            if not letter:
                continue

            if letter in word:
                update_board(word, board, letter)
                print("Correct!")
            else:
                attempts += 1
                remaining = max_attempts - attempts
                print(f"Wrong. {remaining} attempts remaining.")
                print(f"Attempts: {attempts}/{max_attempts}")

    except Exception as e:
        print(f"Unexpected error: {e}")

    if "_" in board:
        print("You lost :(")
        show_hangman()
        return

    print(f"You won! The word was: {word}")


if __name__ == "__main__":
    play_hangman()
