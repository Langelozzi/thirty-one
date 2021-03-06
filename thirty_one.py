# Author: Lucas Angelozzi
# Date: 05/03/22
# Purpose: The card game 31 as a personal project

# Imports
from cards_module.standard_deck import Deck
from thirty_one_hand import TO_Hand
from cards_module.card import Card
from collections import Counter
import os
import time

def create_deck() -> list:
    deck = Deck()
    deck.remove_jokers()
    deck.add_values_ace_eleven()
    deck.shuffle()

    return deck.cards

def calculate_hand_total(hand: list) -> int:
    suits_in_hand = [card.suit for card in hand]
    
    counter = Counter(suits_in_hand)
    # when there was more than one suit in here then it would add all the cards from both suits so i had to make it that it only uses the first suit in the list
    same_suit = [key for key in counter.keys() if counter[key] > 1]
    
    try:                                                            # first suit only [0]
        hand_value = [card.value for card in hand if card.suit == same_suit[0]]
        total = sum(hand_value)
        return total
    except IndexError:
        return max([card.value for card in hand])


def determine_worst_card(hand: list) -> Card:
    suits_in_hand = [card.suit for card in hand]
    
    counter = Counter(suits_in_hand)
    same_suit = [key for key in counter.keys() if counter[key] > 1]
    
    try:
        # returning the card object that has the lowest value of all the cards with unique suits
        non_same_card_values = [card.value for card in hand if card.suit != same_suit[0]]
        return [card for card in hand if card.value == min(non_same_card_values)][0]
    except:
        # returning the card object that has the lowest value of all the cards
        return [card for card in hand if card.value == min([card.value for card in hand])][0]


def comp_turn(numb: int, hand: TO_Hand, disc_card: Card, disc_pile: list, deck: list, deck_card: Card, k: int) -> bool:
    print(f"\nComputer {numb} is taking their turn...")
    time.sleep(1)

    hand_w_disc = hand.hand.copy()
    hand_w_disc.append(disc_card)
    disc_pile.remove(disc_card)

    if calculate_hand_total(hand_w_disc) > hand.calculate_hand_total():
        print(f"Computer {numb} drew from the discard pile")
        time.sleep(1)
        print(f"Computer {numb} has discarded a card")
        time.sleep(1)
        hand = hand_w_disc

        disc_card = determine_worst_card(hand)
        hand.remove(disc_card)
        disc_pile.append(disc_card)
    
    else:
        print(f"Computer {numb} drew from the deck")
        time.sleep(1)
        print(f"Computer {numb} has discarded a card\n")
        time.sleep(1)
        hand.add_card(deck_card)
        
        if deck_card in deck:
            deck.remove(deck_card)

        disc_card = determine_worst_card(hand.hand)
        hand.remove_card(disc_card)
        disc_pile.append(disc_card)

        hand = hand.hand

    if k == 1:
        hand_total = calculate_hand_total(hand)
        if hand_total > 26:
            print(f"Computer {numb} has knocked, you have one turn left\n")
            time.sleep(3)
            return True, disc_card, disc_pile, deck, deck_card
        else:
            return False, disc_card, disc_pile, deck, deck_card

    return False, disc_card, disc_pile, deck, deck_card

def player_turn(player_hand: TO_Hand, discard_card: Card, discard_pile: list, deck: list, top_deck_card: Card, k: int):
    print(f"<---------- Your Cards ---------->")
    player_hand.print_hand()
    print(f"Current Hand Value: {player_hand.calculate_hand_total()}\n")
    
    print(f"<---------- Card Options ---------->")
    print(f"Discarded Card: {discard_card}")
    print(f"Deck Card: [?]")

    print(f"\n<---------- Draw Card ---------->")
    option = input("Would you like to draw from the discard pile or from the deck?: ")
    while option.lower() not in ("discard", "discard pile", "dp", "deck", "deck pile", "card pile"):
        option = input("Please input a valid option (discard or deck): ")

    if option.lower() in ("discard", "discard pile", "dp"):
        player_hand.add_card(discard_card)
        discard_pile.remove(discard_card)
    elif option.lower() in ("deck", "deck pile", "card pile"):
        player_hand.add_card(top_deck_card)
        deck.remove(top_deck_card)

    print(f"\n<---------- Your Cards ---------->")
    player_hand.print_hand()
    print(f"Current Hand Value: {player_hand.calculate_hand_total()}\n")

    discard_option = int(input("Which card would you like to discard of?: "))
    while type(discard_option) is not int or discard_option not in (1,2,3,4):
        discard_option = int(input("Must choose a number between 1-4 when discarding a card. Pick again: "))

    discard_card = player_hand.remove_card(player_hand.hand[discard_option-1])
    discard_pile.append(discard_card)
    
    if k == 1:
        knocked = input("\nWould you like to knock?: ")
        if knocked.lower() in ("yes", "y", "ye", "yea", "yeah"):
            return True, discard_card, discard_pile, deck, top_deck_card
        elif knocked.lower() in ("no", "n", "nah"):
            return False, discard_card, discard_pile, deck, top_deck_card

    return False, discard_card, discard_pile, deck, top_deck_card

def clear_console():
    # if on windows
    if os.name in ('nt', 'dos'):
        os.system('cls')
    # if on mac or linux
    else:
        os.system('clear')

def determine_winner(p_hand: TO_Hand, c1_hand: TO_Hand, c2_hand: TO_Hand, c3_hand: TO_Hand):
    p1_total = p_hand.calculate_hand_total()
    c1_total = c1_hand.calculate_hand_total()
    c2_total = c2_hand.calculate_hand_total()
    c3_total = c3_hand.calculate_hand_total()

    highest_score = max(p1_total, c1_total, c2_total, c3_total)
    
    print("<---------- Final Scores ---------->")
    print(f"Your Final Score: {p1_total}")
    print(f"Computer 1 Score: {c1_total}")
    print(f"Computer 2 Score: {c2_total}")
    print(f"Computer 3 Score: {c3_total}")

    if p1_total == highest_score:
        print("\nYou Win!")
    elif c1_total == highest_score:
        print("\nComputer 1 Wins.")
    elif c2_total == highest_score:
        print("\nComputer 2 Wins.")
    elif c2_total == highest_score:
        print("\nComputer 3 Wins.")


def main() -> None:
    # BUGG: Got a discard card that was the same card as the one in my hand
    
    clear_console()
    deck = create_deck()
    player_hand = TO_Hand(deck)
    comp1_hand = TO_Hand(deck)
    comp2_hand = TO_Hand(deck)
    comp3_hand = TO_Hand(deck)
    discard_pile = []
    discard_pile.append(deck[0::-1][0])
    deck.remove(deck[0::-1][0])

    discard_card = discard_pile[::-1][0]

    knock = 1
    p_knocked, c1_knocked, c2_knocked, c3_knocked = [False, False, False, False]
    
    while knock > 0 and len(deck) > 0:
        top_deck_card = deck[::-1][0]
        
        if p_knocked or c1_knocked or c2_knocked or c3_knocked:
            knock -= 1
        p_knocked, discard_card, discard_pile, deck, top_deck_card = player_turn(player_hand, discard_card, discard_pile, deck, top_deck_card, knock)
        clear_console()
        
        if p_knocked or c1_knocked or c2_knocked or c3_knocked:
            knock -= 1
        c1_knocked, discard_card, discard_pile, deck, top_deck_card = comp_turn(1, comp1_hand, discard_card, discard_pile, deck, top_deck_card, knock)
        clear_console()
        
        if p_knocked or c1_knocked or c2_knocked or c3_knocked:
            knock -= 1
        c2_knocked, discard_card, discard_pile, deck, top_deck_card = comp_turn(2, comp2_hand, discard_card, discard_pile, deck, top_deck_card, knock)
        clear_console()
        
        if p_knocked or c1_knocked or c2_knocked or c3_knocked:
            knock -= 1
        c3_knocked, discard_card, discard_pile, deck, top_deck_card = comp_turn(3, comp3_hand, discard_card, discard_pile, deck, top_deck_card, knock)
        clear_console()

    determine_winner(player_hand, comp1_hand, comp2_hand, comp3_hand)
    
        

if __name__ == "__main__":
    main()