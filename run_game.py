
# local imports
from snap import game, ask_for_number_of_players

# external imports
import os


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nWelcome to SNAP simulator!", end='\n')
    n_players = ask_for_number_of_players()
    game(n_players=n_players)
