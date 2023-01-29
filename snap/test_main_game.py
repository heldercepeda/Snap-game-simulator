from unittest import TestCase
from unittest.mock import patch
from inspect import stack

from snap.main_game import Game


class TestGame(TestCase):
    @patch('builtins.input')
    def setUp(self, m_input) -> None:
        max_decks = 3
        testing_scenarios = [
            {
                "players": player,
                "n_decks": n_decks,
                'name_1': 'Player 1',
                'name_2': 'Player 2',
                'name_3': 'Player 3',
                'name_4': 'Player 4'
            } for player in [n for n in range(2, 5)] for n_decks in [str(m) for m in range(1, max_decks + 1)]
        ]
        for s in testing_scenarios:
            m_input.side_effect = [s['n_decks'], s['name_1'], s['name_2'], s['name_3'], s['name_4']]
            self.test_game = Game(n_players=s['players'], testing=True)
            self.test_game_round()

    def test_game_round(self) -> None:
        """
        Check if no cards are missing or duplicated after game.
        Number of cards after combining all three piles from each user must be equal to starting number of cards

        :return:
        """
        all_cards = [c for p in self.test_game.players for c in p.face_down_pile] + \
                    [c for p in self.test_game.players for c in p.face_up_pile] + \
                    [c for p in self.test_game.players for c in p.winning_pile]

        self.assertEqual(len(all_cards), self.test_game.card_decks * 52)
