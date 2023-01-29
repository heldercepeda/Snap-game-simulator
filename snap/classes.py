
# external imports
from random import choice, shuffle
from typing import List, Union
from uuid import uuid4


class Card:
    def __init__(self, suit: str, rank: str):
        """
        Class to represent each card in the deck. Each card will have an id, associated with the belonging deck

        :param suit: Must be clubs, diamonds, hearts or spades
        :param rank: Must be A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2.
                     We just need to compare if rank is the same so str will work
        """
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.__class__.__name__}({self.suit}, {self. rank})"

    def __str__(self):
        return f"| {self.rank} : {self.suit[0].upper()} |"


class Deck:
    def __init__(self):
        """
        Class to represent a deck of cards. Each deck will have a unique id to be used when wrapping up
        """
        self.deck = [Card(suit=s, rank=r) for s in Deck.suits for r in Deck.ranks]

    def shuffle_deck(self) -> List[Card]:
        """
        Shuffles deck of cards to insure randomness when distributing cards

        :return: None
        """
        shuffle(self.deck)
        return self.deck

    suits = ["clubs", "diamonds", "hearts", "spades"]
    ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]


class Player:
    def __init__(self, name: str):
        """
        Class to represent each player

        :param name: Player's name
        """
        self.name = name
        self.face_down_pile: List[Card] = []
        self.face_up_pile: List[Card] = []
        self.winning_pile: List[Card] = []
        self.playing_card: Union[Card, None] = None

    def reaction_time(self) -> int:
        """
        Function will be used to decide which player will win

        :return: int to be compared with other player's reaction time (smallest will win)
        """
        return choice([_ for _ in range(12)])
