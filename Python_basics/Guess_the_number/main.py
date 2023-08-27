from art import logo
import random

EASY_LEVEL = 10
MEDIUM_LEVEL = 7
HARD_LEVEL = 5

def check_answer(guess, answer, turns):
    """
        Compare the user's guess with the correct answer and provide feedback based on the comparison.

        Parameters:
        guess (int): The user's guess.
        answer (int): The correct answer.
        turns (int): The number of remaining attempts.

        Returns:
        int: The updated number of remaining attempts.
    """
    if guess > answer:
        print("Too high. Try again.")
        return turns - 1
    elif guess < answer:
        print("Too low. Try angain.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def setdificulty():
    """
        Prompts the user to choose a difficulty level for the game and returns the corresponding level constant.

        Returns:
            int: The chosen difficulty level constant (EASY_LEVEL, MEDIUM_LEVEL, or HARD_LEVEL).

        Example Usage:
            level = setdificulty()
    """
    while True:
        level = input("Choose a difficulty, Type 'easy', 'medium' or 'hard': ")
        if level.lower() == 'easy':
            return EASY_LEVEL
        elif level.lower() == 'medium':
            return MEDIUM_LEVEL
        elif level.lower() == 'hard':
            return HARD_LEVEL
        else:
            print("Please choose a valid option.")


def main ():
    """
        The main function is the main entry point of the Number Guessing Game. 
        It initializes the game, prompts the user for guesses, 
        and checks if the guess is correct.

        Inputs:
        None

        Outputs:
        None
    """
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = setdificulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
        elif guess != answer:
            print("Guess again.")


if __name__ == '__main__':
    main()