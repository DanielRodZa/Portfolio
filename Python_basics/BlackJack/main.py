from art import logo
from baraja import baraja, baraja_blackjack
import os
import random

boolean = [True, False]

def clearScreen():
    os_name = os.name

    if os_name == 'posix':
        os.system('clear')
    elif os_name == 'nt':
        os.system('cls')

def get_valid_init():
    while True:
        init = str(input("Do you want to play a game of BlackJack? Type 'y' or 'n': "))
        if init.lower() == 'y':
            return True
        elif init.lower() == 'n':
            return False
        else:
            print("Plase enter a valid option.")


def select_two_cards(selected_cards):
    cards = []
    while len(cards) != 2:
        card = random.choice(baraja)
        if card not in selected_cards:
            cards.append(card)
            selected_cards.append(card)
    return cards

def select_valid_deal_option():
    while True:
        option = input("Do you want an other card: ")
        if option == 'y':
            return True
        elif option == 'n':
            return False
        else:
            print("Please select a valid option")

def deal_card(user_cards, selected_cards):
    while True:
        card = random.choice(baraja)
        if card not in selected_cards:
            user_cards.append(card)
            selected_cards.append(card)
            return user_cards


def score_obtain(cards):
    score = 0
    for card in cards:
        for key, value in baraja_blackjack.items():
            if card in value:
                score += key
    return score

def is_blackjack(cards):
    if score_obtain(cards) == 21:
        return True
    else:
        return False

def compare_scores(user_score, dealer_score):
    if user_score == dealer_score:
        return 'tie'
    elif (user_score > dealer_score and user_score <= 21) or dealer_score > 21:
        return 'user'
    elif user_score < dealer_score and dealer_score <= 21:
        return 'dealer'


def select_continue():
    while True:
        cont = str(input("Want an other game?('y/n'): "))
        if cont.lower() == 'y':
            return True
        elif cont.lower() == 'n':
            return False
        else:
            print('Please select a valid option.')


def main():
    init = get_valid_init()
    while init:
        clearScreen()
        print(logo)
        selected_cards = []

        user_cards = select_two_cards(selected_cards)
        user_score = score_obtain(user_cards)
        dealer_cards = select_two_cards(selected_cards)
        dealer_score = score_obtain(dealer_cards)

        user_blackjack = is_blackjack(user_cards)
        if user_blackjack:
            print("You won with a blackjack!")
            break

        dealer_blackjack = is_blackjack(dealer_cards)
        if dealer_blackjack:
            print("You lose, dealer have blackjack!")
            break

        print(f'User cards {", ".join(user_cards)} with score: {user_score}')
        print(f'Dealer cards "UNKNOWN" {", ".join(dealer_cards[1:])} with score: {score_obtain(dealer_cards[1:])}')

        option = select_valid_deal_option()

        while option and not user_blackjack and not dealer_blackjack:
            print('Dealing a card for user...')
            user_cards = deal_card(user_cards, selected_cards)
            user_score = score_obtain(user_cards)
            print(f'User cards {", ".join(user_cards)} with score: {user_score}')

            if user_score <= 21:
                option = select_valid_deal_option()
            else:
                print('You went over. You lose')
                break

        while dealer_score <= 14:
            print("Dealer have 14 or less in score, dealing a card...")
            dealer_cards = deal_card(dealer_cards, selected_cards)
            dealer_score = score_obtain(dealer_cards)
            print(f'Dealer cards "UNKNOWN"{", ".join(dealer_cards[1:])} with score: {score_obtain(dealer_cards[1:])}')

        dealer_choice = random.choice(boolean)
        while dealer_score < 21 and dealer_choice and not user_blackjack and not dealer_blackjack:
            dealer_cards = deal_card(dealer_cards, selected_cards)
            print('Dealing a card for dealer...')
            print(f'Dealer cards {", ".join(dealer_cards)} with score: {score_obtain(dealer_cards[1:])}')
            dealer_choice = random.choice(boolean)
            dealer_score = score_obtain(dealer_cards)
            if dealer_score >= 21:
                break


        result = compare_scores(user_score, dealer_score)
        if result == 'tie':
            print("There is a tie.")
        if result == 'user':
            print("Your won!")
        if result == 'dealer':
            print("You lose!")

        print(f"User has {', '.join(user_cards)} with score {user_score}")
        print(f"Dealer has {', '.join(dealer_cards)} with score {dealer_score}")

        init = select_continue()


if __name__ == '__main__':
    main()