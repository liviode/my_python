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


card_rank = [
    {'value': 11, 'name': 'Ass'},
    {'value': 4, 'name': 'König'},
    {'value': 3, 'name': 'Ober'},
    {'value': 2, 'name': 'Under'},
    {'value': 10, 'name': 'Banner'},
    {'value': 0, 'name': 'Nüüni'},
    {'value': 0, 'name': 'Achti'},
    {'value': 0, 'name': 'Sibni'},
    {'value': 0, 'name': 'Sächsi'}
]

_card_values = [11, 4, 3, 2, 10, 0, 0, 0, 0]
_card_values_top = [11, 4, 3, 2, 10, 0, 8, 0, 0]
_card_values_bottom = [0, 4, 3, 2, 10, 0, 8, 0, 11]
_card_values_trumpf = [11, 4, 3, 20, 10, 14, 0, 0, 0]

_card_codes = ['As', 'Kö', 'Ob', 'Un', 'Ba', '09', '08', '07', '06']

_card_color_names = ['SE', 'SI', 'RO', 'EI']


def to_card(card_code, color_name):
    rank = _card_codes.index(card_code)
    color = _card_color_names.index(color_name)
    return pow(9, color) + rank


def card_to_code(card):
    return _card_color_names[card // 9] + ' ' + _card_codes[card % 9]


def card_rank(card):
    return card % 9


def card_color_of(card):
    return card // 9


def card_value_of(card, trumpf_card):
    rank = card % 9
    trumpf_rank = card % 9
    if (trumpf_rank == 0):
        return _card_values_top(rank)
    if (trumpf_rank == 8):
        return _card_values_bottom(card % 9)
    if (card // 9 == trumpf_card // 9):
        return _card_values_trumpf(rank)
    return _card_values(rank)


def card_description(card, trumpf_card):
    """Returns a description of the card"""
    pass


def card_value(card, trumpf_card):
    """Returns the value of the card"""
    pass


def winner_card(card1, card2, trumpf_card):
    pass


# see : https://docs.python.org/3/library/random.html
def random_card_set(max=36):
    for i in range(max):
        card = random.randrange(0, max)


def random_card_set2(max=36):
    new_card_set = range(max)
    return random.sample(new_card_set, k=36)


print(random_card_set2())
