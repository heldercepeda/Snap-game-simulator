
# local imports
from snap.main_game import Game


"""
Module "snap" __init__ file

Our application only requires one class and the bellow function
"""


def ask_for_number_of_players() -> int:
    """
    Function responsible for asking number of players in game
    No exception will be raised, function will repeat until it gets a valid input

    :return: Number of players
    """
    while True:
        n_players = input('How many players will be playing (min=2, max=4)?\n')
        try:
            n_players = int(n_players)
        except Exception as e:
            print('Please enter a integer', end='\n')
        else:
            if not 2 <= n_players <= 4:
                print('Please enter a number between 2 and 4', end='\n')
            else:
                break
    return n_players


"""
Object to be imported in run_game.py
"""
game = Game
