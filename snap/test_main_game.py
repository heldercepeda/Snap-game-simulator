
# external imports
from unittest import TestCase
from unittest.mock import patch

# local imports
from snap.main_game import Game


class TestGame(TestCase):

    @classmethod
    @patch('builtins.input')
    def setUpClass(cls, m_input) -> None:
        """
        Function will run once before any test in the class simulating a game using different scenarios
        Each game will be store in a list (scenarios) that will be used to run test(s) into

        :param m_input: Part of @patch requirements so we can simulate different input
        :return:
        """
        super(TestGame, cls).setUpClass()
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
        scenarios = []
        for s in testing_scenarios:
            m_input.side_effect = [s['n_decks'], s['name_1'], s['name_2'], s['name_3'], s['name_4']]
            scenarios.append(Game(n_players=s['players'], testing=True))
        cls.scenarios = scenarios

    def test_game_round(self) -> None:
        """
        Check if no cards are missing or duplicated after game.
        Number of cards after combining all three piles from each user must be equal to starting number of cards

        :return:
        """
        for scenario in self.scenarios:
            all_cards = [c for p in scenario.players for c in p.face_down_pile] + \
                        [c for p in scenario.players for c in p.face_up_pile] + \
                        [c for p in scenario.players for c in p.winning_pile]

            self.assertEqual(len(all_cards), scenario.card_decks * 52)
