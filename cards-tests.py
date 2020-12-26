#  Shuffle Cards for player Spieler A and B
import cards

# Array
a = [[1, 2, 3], [4, 5, 6]]
print(a[0])
print(a[1])

print(cards.random_card_set())

new_game = cards.TwoPlayerJassStatus(100, 666)

new_game.dump()


print(cards.card_to_code(3))
