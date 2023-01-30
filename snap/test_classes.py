
# external imports
from unittest import TestCase

# local imports
from snap.classes import Player, Deck


class TestPlayer(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """
        Function will run once before any test in the class.
        It will create a testing player (test_player) to be used when running test functions

        :return:
        """
        super(TestPlayer, cls).setUpClass()
        cls.test_player = Player(name='testing')

    def test_init(self) -> None:
        """
        Testing necessary properties and types

        :return:
        """
        for p in ['winning_pile', 'face_down_pile', 'face_up_pile']:
            self.assertIn(p, dir(self.test_player))
            self.assertIsInstance(getattr(self.test_player, p), list)

    def test_reaction_time(self) -> None:
        """
        Testing reaction time for given player

        :return:
        """
        self.assertIsInstance(self.test_player.reaction_time(), int)


class TestDeck(TestCase):
    def setUp(self) -> None:
        """
        Function creates a card deck (test_deck) to be used when running tests
        There is only on test function in the class, so no need to use setUpClass

        :return:
        """
        self.test_deck = Deck()

    def test_shuffle_deck(self) -> None:
        """
        Testing shuffle method

        :return:
        """
        deck_1 = [(c.rank, c.suit) for c in self.test_deck.deck]
        deck_2 = [(c.rank, c.suit) for c in self.test_deck.shuffle_deck()]
        self.assertNotEqual(deck_1, deck_2)
        self.assertCountEqual(deck_1, deck_2)
