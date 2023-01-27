
# external imports
from random import choice, shuffle
from typing import List, Union
from uuid import uuid4


class Card:
    def __init__(self, u_id: str, suit: str, rank: str):
        """
        Class to represent each card in the deck.

        :param suit: Must be clubs, diamonds, hearts or spades
        :param rank: Must be A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2.
                     We just need to compare if rank is the same so str will work
        """
        self.suit = suit
        self.rank = rank
        self.id = u_id

    def __repr__(self):
        return f"{self.__class__.__name__}({self.suit}, {self. rank})"

    def __str__(self):
        return f"| {self.rank} : {self.suit[0].upper()} |"


class Deck:
    def __init__(self):
        """
        Class to represent a deck of cards
        """
        self.id = uuid4().hex
        self.deck = [Card(u_id=self.id, suit=s, rank=r) for s in Deck.suits for r in Deck.ranks]
        self.shuffle_deck()


    def shuffle_deck(self) -> None:
        """
        Shuffles deck of cards to insure randomness when distributing cards

        :return: None
        """
        shuffle(self.deck)

    suits = ["clubs", "diamonds", "hearts", "spades"]
    ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]


class Player:
    def __init__(self, name: str, card_decks: int, level: int = 1):
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
        self.face_up_pile: List[Card] = []
        self.winning_pile: List[Card] = []
        self.playing_card: Union[Card, None] = None

    def reaction_time(self) -> int:
        """
        Function will be used to decide which player will win

        :return: int to be compared with other player's reaction time (smallest will win)
        """
        return choice([_ for _ in range(12 // self.level)])
