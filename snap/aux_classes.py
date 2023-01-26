
from random import choice
from typing import List


class Card:
    def __init__(self, suit: str, rank: str):
        """
        Class to represent each card in the deck.

        :param suit: Must be clubs, diamonds, hearts or spades
        :param rank: Must be A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2. We just need to compare if rank is the same so str is fine
        """
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.__class__.__name__}({self.suit}, {self. rank})"

    def __str__(self):
        return f"|{self.rank}:{self.suit[0].upper()}|"


class Deck:
    pass


class Player:
    def __init__(self, name: str, level: int = 1):
        """
        Class to represent each player

        :param name: Player's name
        :param level: Player's level. Must be 1, 2 or 3 and highest level will have the lowest reaction time
        """
        assert level in [1, 2, 3]
        assert name.strip()
        self.name = name
        self.level = level
        self.face_down_pile: List[Card] = []

    def reaction_time(self) -> int:
        """
        Function will be used to decide which player will win

        :return: int to be compared with other player's reaction time (smallest will win)
        """
        return choice([_ for _ in range(12 // self.level)])

