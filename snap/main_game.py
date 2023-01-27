
# local imports
from snap.classes import Deck, Player

# external imports
from typing import List


class Game:
    def __init__(self, n_players: int = 3):
        self.n_players = n_players
        self.players: List[Player] = []
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
        for _ in range(n_players):
            _name = ""
            while not _name:
                _name = input(f"Player's {_ + 1} name: ").strip()
            self.players.append(Player(name=_name, card_decks=self.card_decks))

        self.playing_decks = [Deck().deck for _ in range(self.card_decks)]
        self.distribute_cards()
        self.play()
        self.results()

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
        i = 1
        while True:
            for player in self.players:
                if player.face_down_pile:
                    player.playing_card = player.face_down_pile.pop()
                    player.face_up_pile.append(player.playing_card)
                else:
                    # player has no cards left on the face_down_pile but still on play
                    continue
                self.compare_playing_cards()
                print([p.face_down_pile.__len__() for p in self.players])
            if all([len(p.face_down_pile) == 0 for p in self.players]):
                break
        return

    def compare_playing_cards(self) -> None:
        showing_cards = [p.playing_card for p in self.players if p.playing_card is not None]
        print([str(_) for _ in showing_cards])
        showing_cards = [p.playing_card.rank for p in self.players if p.playing_card is not None]

        if len(showing_cards) != len(set(showing_cards)):
            while True:
                # in this case it can not be a draw so reaction times will be calculated again
                # if first two lower reaction times are equal
                # Not totally fair but is fine for now
                reaction_times = [(p.reaction_time(), p) for p in self.players]
                reaction_times.sort(key=lambda x: x[0])
                if len([_[0] for _ in reaction_times[:2]]) == len(set([_[0] for _ in reaction_times[:2]])):
                    break
                else:
                    continue

            winner = reaction_times[0][1]
            print(winner.name)
            # print(winner.winning_pile)
            winner.winning_pile.extend([c for p in self.players for c in p.face_up_pile])
            # print(winner.winning_pile)
            # print('\n')

            for p in self.players:
                p.face_up_pile = []
                p.playing_card = None

    def results(self):
        print('\n')
        for p in self.players:
            print(f"Player's name: {p.name}")
            print(f"Number of cards in winning pile: {len(p.winning_pile)}")

