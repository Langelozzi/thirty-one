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

def calculate_hand_total(hand: list) -> int:
    suits_in_hand = [card.suit for card in hand]
    
    counter = Counter(suits_in_hand)
    same_suit = [key for key in counter.keys() if counter[key] > 1]
    
    hand_value = [card.value for card in hand if card.suit in same_suit]
    total = sum(hand_value)

    if total > 0:
        return total
    else:
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

# work in progress
def comp_turn(hand: TO_Hand, disc_card: Card, disc_pile: list, deck: list, deck_card: Card, k: bool) -> bool:
    print("\nComputer 1 is taking their turn...\n")

    hand_w_disc = hand.hand.copy()
    hand_w_disc.append(disc_card)
    disc_pile.remove(disc_card)

    if calculate_hand_total(hand_w_disc) > hand.calculate_hand_total():
        hand = hand_w_disc

        worst_card = determine_worst_card(hand)
        hand.remove(worst_card)
        disc_pile.append(worst_card)
    else:
        hand.add_card(deck_card)
        
        if deck_card in deck:
            deck.remove(deck_card)

        worst_card = determine_worst_card(hand.hand)
        hand.remove_card(worst_card)
        disc_pile.append(worst_card)

        hand = hand.hand

    if not k or k == False:
        hand_total = calculate_hand_total(hand)
        if hand_total > 10:
            print("Computer 1 has knocked, you have one turn left\n")
            return True
        else:
            return False

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

    print(f"\n<---------- Your Cards ---------->")
    player_hand.print_hand()
    print(f"Current Hand Value: {player_hand.calculate_hand_total()}\n")

    discard_option = int(input("Which card would you like to discard of?: "))
    discard_card = player_hand.remove_card(player_hand.hand[discard_option-1])
    discard_pile.append(discard_card)
    
    if not k or k == False:
        knocked = input("\nWould you like to knock?: ")
        if knocked.lower() in ("yes", "y", "ye", "yea", "yeah"):
            return True, discard_card, discard_pile, deck, top_deck_card
        elif knocked.lower() in ("no", "n", "nah"):
            return False, discard_card, discard_pile, deck, top_deck_card

    return False, discard_card, discard_pile, deck, top_deck_card


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

        top_deck_card = deck[::-1][0]
        discard_card = discard_pile[::-1][0]
        
        knocked, discard_card, discard_pile, deck, top_deck_card = player_turn(player_hand, discard_card, discard_pile, deck, top_deck_card, knocked)
        knocked = comp_turn(comp1_hand, discard_card, discard_pile, deck, top_deck_card, knocked)
        

if __name__ == "__main__":
    main()