# Author: Lucas Angelozzi
# Date: 05/03/22
# Purpose: The card game 31 as a personal project

# Imports
from cards_module.standard_deck import Deck
from thirty_one_hand import TO_Hand
from cards_module.card import Card
from collections import Counter

def create_deck() -> list:
    deck = Deck()
    deck.remove_jokers()
    deck.add_values_ace_eleven()
    deck.shuffle()

    return deck.cards

def calculate_hand_total(hand) -> int:
    suits_in_hand = [card.suit for card in hand]
    
    counter = Counter(suits_in_hand)
    same_suit = [key for key in counter.keys() if counter[key] > 1]
    
    hand_value = [card.value for card in hand if card.suit in same_suit]
    total = sum(hand_value)

    if total > 0:
        return total
    else:
        return max([card.value for card in hand])

def comp_turn(deck: list, hand: TO_Hand, disc_pile: list, disc_card: Card, deck_card: Card):
        hand_w_disc = hand.hand.copy().append(disc_card)

        if calculate_hand_total(hand_w_disc) > hand.calculate_hand_total():
            hand.add_card(disc_card)
            disc_pile.remove(disc_card)

        else:
            hand.add_card(deck_card)
            deck.remove(deck_card)

def player_turn(player_hand: TO_Hand, discard_card: Card, discard_pile: list, deck: list, top_deck_card: Card, k: bool):
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

    print(f"<---------- Your Cards ---------->")
    player_hand.print_hand()
    print(f"Current Hand Value: {player_hand.calculate_hand_total()}\n")

    discard_option = int(input("Which card would you like to discard of?: "))
    chosen_card = player_hand.remove_card(player_hand.hand[discard_option-1])
    discard_pile.append(chosen_card)   
    
    if not k:
        knocked = input("\nWould you like to knock?: ")
        if knocked.lower() in ("yes", "y", "ye", "yea", "yeah"):
            return True
        elif knocked.lower() in ("no", "n", "nah"):
            return False


def main() -> None:
    deck = create_deck()
    player_hand = TO_Hand(deck)
    comp1_hand = TO_Hand(deck)
    discard_pile = []
    discard_pile.append(deck[0::-1][0])
    deck.remove(deck[0::-1][0])

    knock = 1
    knocked = False
    
    while knock > 0:
        if knocked:
            knock -= 1

        top_deck_card = deck[0::-1][0]
        discard_card = discard_pile[::-1][0]
        
        knocked = player_turn(player_hand, discard_card, discard_pile, deck, top_deck_card, knocked)

        
        

if __name__ == "__main__":
    main()