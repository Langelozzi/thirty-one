# Author: Lucas Angelozzi
# Date: 05/03/22
# Purpose: The card game 31 as a personal project

# Imports
from cards_module.standard_deck import Deck
from thirty_one_hand import TO_Hand
from cards_module.card import Card

def create_deck() -> list:
    deck = Deck()
    deck.remove_jokers()
    deck.add_values_ace_eleven()
    deck.shuffle()

    return deck.cards

def main() -> None:
    deck = create_deck()
    player_hand = TO_Hand(deck)
    comp1_hand = TO_Hand(deck)
    discard_pile = []
    discard_pile.append(deck[0::-1][0])
    deck.remove(deck[0::-1][0])

    knock = False
    
    for i in range(0, 5):
        top_deck_card = deck[0::-1][0]
        discard_card = discard_pile[::-1][0]
        
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
        

if __name__ == "__main__":
    main()