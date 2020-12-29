import random


class TwoPlayerJassStatus:
    """Class representing the game status of a two player Jass"""

    def __init__(self, player1, player2):
        self.cards = [[], [], [], []]
        new_card_set = random_card_set2()
        for i in range(len(new_card_set) // 4):
            self.cards[0].append(new_card_set[i])
            self.cards[1].append(new_card_set[i + 9])
            self.cards[2].append(new_card_set[i + 18])
            self.cards[3].append(new_card_set[i + 27])
        self.current_player_index = 0
        self.players = [player1, player2]
        self.card_on_table = None
        self.stacks = [[], []]

    def trumpf_card(self):
        return self.cards[3][8]

    def dump(self):
        print('player 1 first round', self.cards[0])
        print('player 2 first round', self.cards[1])
        print('player 1 second round', self.cards[2])
        print('player 2 second round', self.cards[3])
        print('trumpf cards', self.trumpf_card())

    def playCardFist(self, player, card):
        pass


    def playCardSecond(self, player, card):
        pass


    def possible_moves(self):
        pass


    def move(self, player, player_card):
        if self.players[self.current_player_index] != player:
            return 'no_your_turn'
        if self.card_on_table is None:
            self.card_on_table = player_card
            self.current_player_index = self.current_player_index + 1 % 2
            return 'card_on_table'
        else:
            wc = winner_card(player_card, self.card_on_table, self.trumpf_card())


    def add_to_stack(self, player, card1, card2):
        ind = self.players.index(player)
        self.stacks[ind].append(card1)
        self.stacks[ind].append(card2)


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
    """Return 0 if card1 is winner 1 otherwise"""
    # TODO Das ist noch falsch

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

    # Wenn trumpf_card 'obe-nabe' ist ...
    # Wenn trumpf_card unde-ufe ist....
    # Wenn trumpf_card normal trumpf ist....


# see : https://docs.python.org/3/library/random.html
def random_card_set(max=36):
    for i in range(max):
        card = random.randrange(0, max)


def random_card_set2(max=36):
    new_card_set = range(max)
    return random.sample(new_card_set, k=36)
