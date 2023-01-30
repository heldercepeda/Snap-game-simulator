
# external imports
from unittest import TestCase
from unittest.mock import patch

# local imports
from snap import ask_for_number_of_players


class Test(TestCase):
    @patch('builtins.input')
    def test_ask_for_number_of_players(self, m_input):
        scenarios = [
            {
                'first_input': _input[0],
                'second_input': _input[1]
            } for _input in [
                ('just a string', 2),
                ('   ', 4),
                ('    2', 2),
                ('3    ', 3),
                ('2', 2),
                ('3', 3),
                ('4', 4)
            ]
        ]

        for scenario in scenarios:
            m_input.side_effect = [scenario['first_input'], scenario['second_input']]
            test_n_players = ask_for_number_of_players()
            self.assertEqual(scenario['second_input'], test_n_players)
