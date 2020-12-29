#  Shuffle Cards for player Spieler A and B
import cards

# shuffle

newGame1 = cards.TwoPlayerJassStatus(123,4456)

newGame2 = cards.TwoPlayerJassStatus(123,4456)


print('**** Game 1 ****')

newGame1.dump()

print('**** Game 2 ****')
newGame2.dump()


##

table = newGame1.playCard(123, 13)

table_win = newGame1.playCard(4456, 27)

