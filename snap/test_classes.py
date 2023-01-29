from unittest import TestCase

from snap.classes import Player, Deck


class TestPlayer(TestCase):
    def setUp(self) -> None:
        self.test_player = Player(name='testing')

    def test_init(self) -> None:
        self.assertIsInstance(self.test_player.winning_pile, list)
        self.assertIsInstance(self.test_player.face_down_pile, list)
        self.assertIsInstance(self.test_player.face_up_pile, list)

    def test_reaction_time(self) -> None:
        self.assertIsInstance(self.test_player.reaction_time(), int)


class TestDeck(TestCase):
    def setUp(self) -> None:
        self.test_deck = Deck()

    def test_shuffle_deck(self) -> None:
        deck_1 = [(c.rank, c.suit) for c in self.test_deck.deck]
        deck_2 = [(c.rank, c.suit) for c in self.test_deck.shuffle_deck()]
        self.assertNotEqual(deck_1, deck_2)
        self.assertCountEqual(deck_1, deck_2)
