#  Shuffle Cards for player Spieler A and B
import cards

# shuffle

newGame1 = cards.Two_Player_Stich_Jass('livio','toni')

newGame2 = cards.Two_Player_Stich_Jass('toni', 'livio')


print('**** Game 1 ****')

newGame1.dump()

# print('**** Game 2 ****')
# newGame2.dump()


##

print('**** Game 1 ****')



print('status livio:', newGame1.status('livio'))








