from art import logo, vs
from game_data import data
import random
import os

def clearScreen():
    os_name = os.name

    if os_name == 'posix':
        os.system('clear')
    elif os_name == 'nt':
        os.system('cls')


def choose_winner(A_selector, B_selector):
    """
        Determines which selector has more followers based on their follower count.

        Args:
            A_selector (dict): A dictionary containing information about the first selector, including their name and follower count.
            B_selector (dict): A dictionary containing information about the second selector, including their name and follower count.

        Returns:
            str: 'a' if A_selector has more followers, 'b' if B_selector has more followers.
    """
    return 'a' if A_selector['follower_count'] > B_selector['follower_count'] else 'b'
    


def main():
    """
        The main function is the main logic of the program. 
        It allows the user to play a game where they compare the number of followers between two randomly selected data entries. 
        The user is prompted to choose which entry has more followers, 
        and their score is updated accordingly. 
        The game continues until the user makes a wrong guess.

    """
    should_continue = True
    score = 0
    A_selector = random.choice(data)
    while should_continue:
        print(logo)
        if score > 0:
            print(f"Your score is: {score}")
        print(f"Compare A: {A_selector['name']},a {A_selector['description']}, from {A_selector['country']}.")
        print(vs)
        B_selector = random.choice(data)
        print(f"Against B: {B_selector['name']},a {B_selector['description']}, from {B_selector['country']}.")
        user= input("\nWho has more followers? Type 'A' or 'B': ")
        more_followers = choose_winner(A_selector, B_selector)
        if user.lower() == more_followers:
            score += 1
            A_selector = B_selector
            clearScreen()
        else:
            print(f"Sorry, that's wrong. Final score: {score}.\nGAME OVER")
            should_continue = False


if __name__ == "__main__":
    main()
