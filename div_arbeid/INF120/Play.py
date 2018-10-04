import random as rng
import time
import os

def play():
	bb = 0
	print "Let's play a game!\nI've chosen a random number between 1 and 10"
	r = rng.randint(1,10)
	while True:
		if bb == 0:
			g = int(raw_input('Guess: '))
			bb += 1
		else:
			g = int(raw_input('Guess again: '))
		if g < r:
			print 'Too low'
		elif g > r:
			print 'Too high'
		elif g == r:
			print 'Correct!'
			time.sleep(1)
			os.system('cls')
			print 'Closing this window in ...3'
			time.sleep(1)
			os.system('cls')
			print 'Closing this window in ..2'
			time.sleep(1)
			os.system('cls')
			print 'Closing this window in .1'
			time.sleep(1)
			break

if __name__ == '__main__':
	play()

