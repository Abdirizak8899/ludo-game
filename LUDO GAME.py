# Ludo game

#copyright of this code has Abdirizak abdullahi hussein

import random

again = True

while again:
	qui = (random.randint(1,6))
	
	stry = int(input('PLAY: '))
	
	if stry == qui:
		print(qui, 'Correct')
	else:
		print('You lose! it is ', qui)