import pytest
from unittest.mock import patch
import random

words = [
    "adventure", "airplane", "astronaut", "bicycle", "butter",
    "butterfly", "carrot", "cheese", "cherry", "chocolate",
    "computer", "development", "dinosaur", "dog", "dragon",
    "elephant", "eleven", "flamingo", "giraffe", "grapes",
    "guitar", "hamburger", "intelligence", "island", "kangaroo",
    "knight", "lemonade", "mermaid", "mouse", "octopus",
    "orange", "orchid", "parrot", "piano", "pineapple",
    "program", "programming", "pumpkin", "seahorse", "spaghetti",
    "strawberry", "submarine", "sun", "telescope", "tiger",
    "umbrella", "universe", "watermelon", "whale", "wine",
    "xylophone", "yoga", "zebra"
]

def choose_word(words):
    """
    This function chooses a random word from a list of words.
    
    Returns:
    - A randomly selected word from the list of words.
    """

    if not words:
        raise ValueError('The "words" list is empty.')

    return random.choice(words)

def show_board(word, guessed_letters):
    """
    Generates a visual representation of the hangman game board.

    Parameters:
    word (str): The secret word that the player is trying to guess.
    guessed_letters (list): A list of letters that the player has already guessed.

    Returns:
    str: The display string representing the current state of the game board.
    """
    if word is None or word == "":
        raise ValueError("Word cannot be None or empty.")
        

    if guessed_letters is None:
        guessed_letters = set()

    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    """
    The main function is the main logic of a hangman game. It chooses a random word, displays a board with hidden letters,
    prompts the user to guess a letter, checks if the letter is correct or incorrect, updates the board, and keeps track of
    the number of attempts. The game continues until the user either guesses the word correctly or runs out of attempts.

    """

    secret_word = choose_word(words)
    guessed_letters = set()
    attempts = 6

    print("¡Welcome to the hangman game!")
    print(show_board(secret_word, guessed_letters))

    while attempts > 0:
        letter = input("Guess a letter: ").lower()

        if not letter.isalpha():
            print("Invalid input. Please enter a letter.")
            continue

        if letter in guessed_letters:
            print("You already guessed that letter..")
            continue

        guessed_letters.add(letter)

        if letter not in secret_word:
            attempts -= 1
            print(f"¡Incorrec! You have {attempts} attempts left.")
            if attempts == 0:
                print(f"You lost! The word was: {secret_word}")
                break
        else:
            print("¡Correct!")
            board = show_board(secret_word, guessed_letters)
            print(board)
            if "_" not in board:
                print("Won! You have guessed the word.")
                break

if __name__ == '__main__':
    main()