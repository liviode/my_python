#  Shuffle Cards for player Spieler A and B
import cards

# Array
a = [[1, 2, 3], [4, 5, 6]]
# print(a[0])
# print(a[1])

# print(cards.random_card_set())
#
# new_game = cards.TwoPlayerJassStatus(100, 666)
# new_game.dump()


print('expected: 1, got:', cards.winner_card(0, 3, 1))

tests = [

    [0, 3, 1, 1],
    [3, 0, 1, 0],
    [3, 0, 10, 1],
    [0, 3, 10, 0],
    # top
    [2, 3, 9, 0],
    [3, 2, 9, 1],
    [1, 18, 9, 0],
    # bottom
    [8, 1, 35, 0],
    [1, 8, 35, 1],
    [8, 8, 35, -1],

]

for test in tests:
    if cards.winner_card(test[0], test[1], test[2]) == test[3]:
        print('Test ok ', test)
    else:
        print('Test not ok!!! ', test)
