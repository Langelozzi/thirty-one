# Author: Lucas Angelozzi
# Date: 04/15/22
# Purpose: Card class for cards module

'''Class for a single card object'''

class Card:
    def __init__(self, suit: str, face: str, value: int=None) -> None:
        """Constructor method. Creates the attributes and does some error checks

        Args:
            suit (str): The suit of the card
            face (str): The face value
            value (int, optional): The actual value of the card. Defaults to None.

        Raises:
            ValueError: if the suit is not valid
            ValueError: if the face is not valid
        """
        
        if (suit not in ["Spade", "Club", "Diamond", "Heart"]
        or type(suit) is not str) :
            raise ValueError
        
        if (face not in 
        ["A",2,3,4,5,6,7,8,9,10,"J","Q", "K", "Jkr"]):
            raise ValueError

        self.suit = suit
        self.face = str(face)
        self.value = value

    def __str__(self) -> str:
        """Returns a stringified representation of a card

        Returns:
            str: the card string
        """
        
        return f"[Suit: {self.suit}, Face: {self.face}, Value: {self.value}]"

    def change_value(self, new_value: int) -> None:
        """Allows you to change the value of a card to a new value

        Args:
            new_value (int): the value you'd like to change the card to
        """
        
        self.value = new_value

    def img(self) -> str:
        # come back to this after
        # 10 causes right side to go off position
        if self.suit == "Spade":
            card_image = f''' 
            ----------------
            |              |
            |              |
            |     {self.suit}    |
            |              |
            |      {self.face}       |
            |              |
            |              |
            |              |
            ----------------

            '''

        return card_image
