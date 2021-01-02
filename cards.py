import random


class Two_Player_Stich_Jass:
    """Class representing the game status of a Two Player Stich Jass"""

    def __init__(self, player1, player2):
        self._cards = [[], [], [], []]
        new_card_set = random_card_set2()
        for i in range(len(new_card_set) // 4):
            self._cards[0].append(new_card_set[i])
            self._cards[1].append(new_card_set[i + 9])
            self._cards[2].append(new_card_set[i + 18])
            self._cards[3].append(new_card_set[i + 27])
        self._current_player_index = 0
        self._players = [player1, player2]
        self._current_player = player1
        self._current_cards = {self._players[0]: self._cards[0], self._players[1]: self._cards[1]}
        self._cards_on_table = []
        self._stacks = {player1: [], player2: []}
        self._round = 0

    def trumpf_card(self):
        return self._cards[3][8]

    def cards_on_table(self):
        return self._cards_on_table

    def players(self) -> list:
        return self._players

    def current_player(self):
        return self._current_player

    def round(self):
        return self._round

    def score(self):
        sc = {}
        sc[self._players[0]] = 0
        sc[self._players[1]] = 0
        return sc

    def player_cards(self, player):
        return self._current_cards[player]

    def playable_cards(self, player):
        return filter_playable_cards(self.player_cards(player), self.trumpf_card(), self.trumpf_card())

    def play_card(self, player, card):
        if player != self._current_player:
            return 'wrong_player'
        if len(self._cards_on_table) == 2:
            self._cards_on_table = []
        other_player = self._players[0] if self._players[0] != player else self._players[1]
        # is the card part of players current cards?
        self._cards_on_table.append({'player': player, 'card': card})
        hand = self._current_cards[player]
        # filter out the card
        new_hand = [c for c in hand if c != card]
        self._current_cards[player] = new_hand
        # if one cards on table...
        if len(self._cards_on_table) == 1:
            self._current_player = other_player
            return 'waiting_for_second_card'
        # if two cards on table...
        if len(self._cards_on_table) == 2:
            w = winner_card(self._cards_on_table[0]['card'], self._cards_on_table[1]['card'], self.trumpf_card())
            if w == 0:
                self._current_player = other_player
                self._stacks[other_player].append(self._cards_on_table[0]['card'])
                self._stacks[other_player].append(self._cards_on_table[1]['card'])
            else:
                self._current_player = player
                self._stacks[player].append(self._cards_on_table[0]['card'])
                self._stacks[player].append(self._cards_on_table[1]['card'])
            if len(self._current_cards[player]) == 0 and len(self._current_cards[other_player]) == 0:
                if self._round == 0:
                    self._round = 1
                    self._current_cards = {self._players[0]: self._cards[2], self._players[1]: self._cards[3]}
                    return 'start_of_second_round'
                else:
                    return 'end_of_game'
            return 'continue'


def dump(self):
    print('player 1 first round', self._cards[0])
    print('player 2 first round', self._cards[1])
    print('player 1 second round', self._cards[2])
    print('player 2 second round', self._cards[3])
    print('trumpf cards', self.trumpf_card())


_card_values = [11, 4, 3, 2, 10, 0, 0, 0, 0]
_card_values_top = [11, 4, 3, 2, 10, 0, 8, 0, 0]
_card_values_bottom = [0, 4, 3, 2, 10, 0, 8, 0, 11]
_card_values_trumpf = [11, 4, 3, 20, 10, 14, 0, 0, 0]
_card_values_trumpf_win = [11, 10, 9, 20, 8, 14, 7, 6, 5]

_card_codes = ['As', 'Kö', 'Ob', 'Un', 'Ba', '09', '08', '07', '06']
# 0 = Schelle Ass
# 1 = Schelle Konig
# ...
# 9 = Schilte Ass
# 10 = Schilte König
# ...
# 35 = Eichle Sechsi
_card_color_names = ['SE', 'SI', 'RO', 'EI']
_card_color_descriptions = ['Schälle', 'Schilte', 'Rose', 'Eichle']
_card_descriptions_trumpf = ['Trumpf Ass', 'Trumpf König', 'Trumpf Ober', 'Trumpf Puur', 'Trumpf Banner', 'Näll',
                             'Trumpf Achti', 'Trumpf Sibni', 'Trumpf Sechsi']
_card_descriptions = ['Ass', 'König', 'Ober', 'Puur', 'Banner', 'Nüüni', 'Achti', 'Sibni', 'Sechsi']


def to_card(card_code, color_name):
    rank = _card_codes.index(card_code)
    color = _card_color_names.index(color_name)
    return pow(9, color) + rank


def card_to_code(card):
    return _card_color_names[card // 9] + '-' + _card_codes[card % 9]


def card_rank(card):
    return card % 9


def card_color_of(card):
    return card // 9


def card_value(card, trumpf_card=None):
    """Returns value of card with trumpf trumpf_card"""
    rank = card % 9
    if trumpf_card == None:
        return _card_values[rank]
    trumpf_rank = trumpf_card % 9
    # Obenabe
    if (trumpf_rank == 0):
        return _card_values_top[rank]
    # Undenufe
    if (trumpf_rank == 8):
        return _card_values_bottom[rank]
    # trumpf
    if ((card // 9) == (trumpf_card // 9)):
        return _card_values_trumpf[rank]
    # normal
    return _card_values[rank]


def card_description(card, trumpf_card=None):
    """Returns a description of the card"""

    color_index = card // 9
    rank_index = card % 9
    if trumpf_card == None:
        return _card_color_descriptions[color_index] + ' ' + _card_descriptions[rank_index]
    pass


def winner_card(card1, card2, trumpf_card):
    """Return 0 if card1 is winner, 1 otherwise."""
    if card1 == card2:
        return -1

    trumpf_color = trumpf_card // 9
    card1_color = card1 // 9
    card2_color = card2 // 9
    # top
    if trumpf_card % 9 == 0:
        if (card1 // 9) == (card2 // 9):
            if (card1 % 9) > (card2 % 9):
                return 1
            else:
                return 0
        return 0
    # bottom
    if trumpf_card % 9 == 8:
        if (card1 // 9) == (card2 // 9):
            if (card1 % 9) < (card2 % 9):
                return 1
            else:
                return 0
        return 0
    # both not trumpf
    if (card1_color != trumpf_color) and (card2_color != trumpf_color):
        if (card1 // 9) == (card2 // 9):
            if (card1 % 9) > (card2 % 9):
                return 1
            else:
                return 0
        return 0
    # card1 trumpf, card2 not trumpf
    if (card1_color == trumpf_color) and (card2_color != trumpf_color):
        return 0
    # card2 trumpf, card1 not trumpf
    if (card1_color != trumpf_color) and (card2_color == trumpf_color):
        return 1
    # card2 trumpf, card1 trumpf
    if (card1_color == trumpf_color) and (card2_color == trumpf_color):
        if _card_values_trumpf_win[card1 % 9] > _card_values_trumpf_win[card2 % 9]:
            return 0
        else:
            return 1
    # never should reach this
    return -1


def filter_playable_cards(cards, table_card, trumpf_card):
    """Returns a sub-set of cards that can be played"""
    if table_card == None:
        return cards
    else:
        new_cards = []
        for card in cards:
            new_cards.append(card)
    return new_cards


# see : https://docs.python.org/3/library/random.html
def random_card_set(max=36):
    for i in range(max):
        card = random.randrange(0, max)


def random_card_set2(max=36):
    new_card_set = range(max)
    return random.sample(new_card_set, k=36)
