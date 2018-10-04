'''
Created on Mar 30, 2012

@author: mariukri
'''
import random as rnd


def one_round(total,strat):
	"""Runs one round with one player, with chosen strat"""
	Rsum = 0
	if strat == "1":
		while True:
			dice = rnd.randint(1,6)
			if dice == 1:
				Rsum = 0
				break
			elif dice == 6:
				Rsum += dice
				break
			else:
				Rsum += dice
	
	elif strat == "2":
		while True:
			dice = rnd.randint(1,6)
			if dice == 1:
				Rsum = 0
				break
			else:
				Rsum += dice
			if Rsum >= 13:
				break
	
	elif strat == "3":
		throw = 0
		while True:
			dice = rnd.randint(1,6)
			if dice == 1:
				Rsum = 0
				break
			elif throw == 4:
				Rsum += dice
				break
			else:
				Rsum += dice
				throw += 1
	
	elif strat == "4":
		dice = rnd.randint(1,6)
		if dice == 1:
			Rsum = 0
		else:
			Rsum = dice

		
	return total + Rsum

	
def one_game(strat_a, strat_b):
	"""Runs one game"""
	total_a = 0
	total_b = 0
	while True:
		total_a = one_round(total_a, strat_a)
		total_b = one_round(total_b, strat_b)
		if total_a >= 63:
			winner = "A"
			break
		elif total_b >= 63:
			winner = "B"
			break
	print "The winner is player %s!" % winner
	return total_a, total_b

	
def play_games(n_games,strat_a, strat_b):
	pass

def printout(result_list):
	"""Prints results"""
	pass

def sample_run():
	play_games(
    
if __name__ == '__main__':
    sample_run()
       
