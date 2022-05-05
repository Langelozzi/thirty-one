# Author: Lucas Angelozzi
# Date: 05/03/22
# Purpose: Hand class for Thirty-One card game

# Imports
from collections import Counter

class TO_Hand:
    def __init__(self, deck: list) -> None:
        # set player hand to top 3 cards in the deck
        player_hand = deck[:3]
        
        # remove the players cards from the deck
        for i in deck[:3]:
            deck.remove(i)
        
        self.hand = player_hand

    def calculate_hand_total(self) -> int:
        # list of the suits in the persons hand
        suits_in_hand = [card.suit for card in self.hand]
        
        # creating a counter which is a dictionary with the value being how many times the key appears in the list
        counter = Counter(suits_in_hand)
        # whichever suit is repeated at least once in the persons hand
        same_suit = [key for key in counter.keys() if counter[key] > 1]
        
        # list of the values that correspond to cards with matching suits
        hand_value = [card.value for card in self.hand if card.suit in same_suit]
        total = sum(hand_value)

        # if there are duplicate suits then the total will be more than 0
        if total > 0:
            return total
        else:
            # if there are no duplicate suits then return the greatest value card as the total
            return max([card.value for card in self.hand])

    def print_hand(self):
        for numb, card in enumerate(self.hand):
            print(f"{numb + 1}: {card}")

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)
        return card