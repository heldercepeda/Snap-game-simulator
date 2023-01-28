
# local imports
from snap.classes import Deck, Player

# external imports
from typing import List
import os
from time import sleep


class Game:
    def __init__(self, n_players: int):
        """
        Class simulates a game of SNAP for a given number of players (between 2 and 4)

        :param n_players: Number of players in the game
        """
        self.n_players = n_players
        self.players: List[Player] = []
        self.card_decks: int = 0
        self.collect_info()
        self.playing_decks = [Deck().deck for _ in range(self.card_decks)]
        self.distribute_cards()
        self.play()
        self.results()

    def collect_info(self) -> None:
        """
        Function to collect needed info before game starts

        :return:
        """
        while True:
            _card_decks = input(f"Number of playing decks: ").strip()
            try:
                _card_decks = int(_card_decks)
            except Exception as e:
                print('Please enter a number')
            else:
                if _card_decks > 0:
                    self.card_decks = _card_decks
                    break
                else:
                    print('Please enter a positive number')
                    continue
        for _ in range(self.n_players):
            _name = ""
            while not _name:
                _name = input(f"Player's {_ + 1} name: ").strip()
            self.players.append(Player(name=_name, card_decks=self.card_decks))


    def distribute_cards(self) -> None:
        """
        Function will distribute the cards and assign the first playing card for users

        :return: None
        """
        # TODO: needs to be improved a bit
        all_cards = [card for deck in self.playing_decks for card in deck]
        _slice = len(all_cards) // self.n_players
        for i, player in enumerate(self.players):
            s = i * _slice
            e = (i + 1) * _slice if not i == len(self.players) - 1 else len(all_cards)
            cards_for_player = all_cards[s:e]
            player.face_down_pile = cards_for_player


    def play(self) -> None:
        """
        Function to simulate a game of SNAP between n players

        :return:
        """
        while True:
            for player in self.players:
                if player.face_down_pile:
                    player.playing_card = player.face_down_pile.pop()
                    player.face_up_pile.append(player.playing_card)
                else:
                    """
                        player has no cards left on the face_down_pile but still on play
                    """
                    continue
                self.compare_playing_cards()
            if all([len(p.face_down_pile) == 0 for p in self.players]):
                """
                    None of the players has cards left
                """
                break
        return

    def compare_playing_cards(self) -> None:
        """
        Function to compare cards in play. Will be executed every time a player show/changes the showing card on top of the face up pile

        :return:
        """
        showing_cards = [p.playing_card for p in self.players if p.playing_card is not None]
        # print([str(_) for _ in showing_cards])

        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n')
        print('Cards on show',end='\n')
        print([str(_) for _ in showing_cards], end='\n\n')
        sleep(0.3)
        showing_cards = [c.rank for c in showing_cards]
        if len(showing_cards) != len(set(showing_cards)):
            while True:
                """
                    In this case it can not be a draw so reaction times will be calculated again
                    if first two lower reaction times are equal
                    Not totally fair but is fine for now
                """

                reaction_times = [(p.reaction_time(), p) for p in self.players]
                reaction_times.sort(key=lambda x: x[0])
                if len([_[0] for _ in reaction_times[:2]]) == len(set([_[0] for _ in reaction_times[:2]])):
                    break
                else:
                    continue

            winner = reaction_times[0][1]
            print(f"{winner.name} wins the round!", end='\n')
            sleep(1)
            winner.winning_pile.extend([c for p in self.players for c in p.face_up_pile])
            """
                Both, face up pile and playing card, need to be reset so the game can continue
            """
            for p in self.players:
                p.face_up_pile = []
                p.playing_card = None

    def results(self) -> None:
        """
        Simple function to print SNAP game results in the terminal

        :return:
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n')
        print("{: >20} {: >20}".format(*["Player's name", '#Winning pile']))
        _aux = [[], 0]
        for p in self.players:
            if len(p.winning_pile) > _aux[1]:
                _aux[0] = []
                _aux[0].append(p.name)
                _aux[1] = len(p.winning_pile)
            elif len(p.winning_pile) == _aux[1]:
                _aux[0].append(p.name)
            _list = [p.name, len(p.winning_pile)]
            print("{: >20} {: >20}".format(*_list))
        print('\n')
        winner = ', '.join(_aux[0])
        print("{: >15} {: >15}".format(*['WINNER' if len(_aux[0]) == 1 else 'WINNERS', winner]))
        print('\n')
