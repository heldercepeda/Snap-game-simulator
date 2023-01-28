
# local imports
from snap import game

# external imports
import os


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nWelcome to SNAP!", end='\n')
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
    game(n_players=n_players)
