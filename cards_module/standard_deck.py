# Author: Lucas Angelozzi
# Date: 04/15/22
# Purpose: Card class for cards module

'''Class for a basic deck. Parent class to any other decks'''

# Imports
from .card import Card
import random

class Deck:
    def __init__(self) -> None:
        """Constructor method. Creates a card object for 52 regular cards and 4 jokers.
        Also creates an attribute for a list of each suit.
        """
        
        faces = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "Jkr"]
        suits = ["Spade", "Heart", "Club", "Diamond"]
        
        self.cards = list()

        for suit in suits:
            for face in faces:
                self.cards.append(Card(suit, face))

        self.spades = [card for card in self.cards if card.suit == "Spade"]
        self.hearts = [card for card in self.cards if card.suit == "Heart"]
        self.clubs = [card for card in self.cards if card.suit == "Club"]
        self.diamonds = [card for card in self.cards if card.suit == "Diamond"]

    def __len__(self) -> int:
        """When the length of the list is queried, returns the number of cards in the deck

        Returns:
            int: how many cards in the deck
        """
        
        return len(self.cards)
    
    def shuffle(self) -> None:
        """Shuffles the deck of cards so that the order is randomized
        """
    
        random.shuffle(self.cards)

    def remove_jokers(self) -> None:
        """Removes all the jokers from the deck
        """
        
        for card in self.cards:
            if card.face == "Jkr":
                self.cards.remove(card)

    def add_values_ace_eleven(self) -> None:
        """Adds values to the cards. 

        Values:
            Ace: 11
            Jack, Queen, King: 10
            1-10: Face value
        """
        
        for card in self.cards:
            if card.face in ("2","3","4","5","6","7","8","9", "10"):
                card.value = int(card.face)
            elif card.face in ("J", "Q", "K"):
                card.value = 10
            elif card.face == "A":
                card.value = 11

    def add_values_ace_one(self) -> None:
        """Adds values to the cards. 

        Values:
            Ace: 11
            Jack, Queen, King: 10
            1-10: Face value
        """
        
        for card in self.cards:
            if card.face in ("2","3","4","5","6","7","8","9", "10"):
                card.value = int(card.face)
            elif card.face in ("J", "Q", "K"):
                card.value = 10
            elif card.face == "A":
                card.value = 1
