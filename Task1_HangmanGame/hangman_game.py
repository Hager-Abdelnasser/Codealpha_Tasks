"""
CodeAlpha Internship - Task 1: Hangman Game
A simple text-based Hangman game.
Concepts: random, while loop, if-else, strings, lists.
"""

import random

WORDS = ["python", "pandas", "database", "pipeline", "analytics"]
MAX_WRONG = 6

STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========""",
]


def display_word(word, guessed):
    """Return the word with unguessed letters hidden as underscores."""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play():
    word = random.choice(WORDS)
    guessed = []          # all letters guessed so far
    wrong = 0

    print("=" * 40)
    print("        WELCOME TO HANGMAN!")
    print("=" * 40)
    print(f"Guess the word, one letter at a time. You have {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        print(STAGES[wrong])
        print("\nWord:", display_word(word, guessed))
        print("Guessed letters:", " ".join(sorted(guessed)) if guessed else "-")
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")

        guess = input("\nEnter a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            wrong += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Win check
        if all(letter in guessed for letter in word):
            print("\nWord:", display_word(word, guessed))
            print("Congratulations, you won!")
            return

    # Loss
    print(STAGES[MAX_WRONG])
    print(f"\nGame over! The word was: {word}")


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
