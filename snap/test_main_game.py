
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
        max_decks = 7
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
        Testing multiple aspects before and after the game happens for each scenario

        :return:
        """
        for scenario in self.scenarios:

            expected_keys = ['face_down_pile', 'face_up_pile', 'winning_pile']
            test_logbook = scenario.logbook
            _keys = sorted(list(test_logbook.keys()))
            """
                logbook must have all expected keys
            """
            for k in _keys:
                _inside_keys = set(list(test_logbook[k].keys()))
                self.assertSetEqual(set(expected_keys), _inside_keys)
            """
                create_log function is only used twice, only two entries are expected in logbook
            """
            self.assertEqual(2, len(_keys))
            """
                all elements in list inside logbook must be int and equal or greater then zero
            """
            for k1 in _keys:
                for k2 in expected_keys:
                    self.assertTrue(all(isinstance(x, int) for x in test_logbook[k1][k2]))
                    self.assertTrue(all(x >= 0 for x in test_logbook[k1][k2]))

            # before game starts
            _key = _keys[0]
            _max = max(test_logbook[_key]['face_down_pile'])
            _min = min(test_logbook[_key]['face_down_pile'])
            """
                Difference between number of cards of each player cannot be greater that 1
            """
            self.assertIn(_max - _min, [0, 1])
            """
                No cards are missing after distributing them
            """
            self.assertEqual(sum(test_logbook[_key]['face_down_pile']), scenario.card_decks * 52)
            """
                face up pile and winning pile must be empty for each player
            """
            self.assertEqual(sum(test_logbook[_key]['face_up_pile']), 0)
            self.assertEqual(sum(test_logbook[_key]['winning_pile']), 0)

            # after game ends
            _key = _keys[1]
            """
                face down pile must be empty for each player
            """
            self.assertEqual(sum(test_logbook[_key]['face_down_pile']), 0)
            """
                summing up everything in face up pile and winning pile for each player must be equal to the total number of cards
            """
            self.assertEqual(
                sum(test_logbook[_key]['face_up_pile']) + sum(test_logbook[_key]['winning_pile']),
                scenario.card_decks * 52
            )
