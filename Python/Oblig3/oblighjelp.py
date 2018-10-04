# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:19:09 2015

@author: montyhatfield
"""

import random

def roll_dice_and_compute_sum(ndice):
    return sum([random.randint(1,6) for i in range(ndice)])

def computer_guess(ndice):
    return random.randint(ndice, 6*ndice)
    

def player_guess(ndice):
    return 7

def play_one_round(ndice, capital, guess_function):
    throw = roll_dice_and_compute_sum(ndice)
    guess = guess_function(ndice)
    if guess == throw:
        capital += guess
    else: 
        capital -= 1
    return capital, throw, guess
    

def play(ngames, nrounds, ndice=2):
    wins = {'Machine' :0, 'Player' :0, 'Draw' :0}
    for i in xrange(ngames):
        player_capital = computer_capital = nrounds # start value
        for j in range(nrounds):
            player_capital, throw, guess = play_one_round(ndice, player_capital, player_guess)
            computer_capital, throw, guess = play_one_round(ndice, computer_capital, computer_guess)
            
        if computer_capital > player_capital:
            winner = 'Machine'
        elif computer_capital < player_capital:
            winner = 'Player'
        else:
            winner = 'Draw'
        wins[winner] += 1 
    return wins

def sample_run():
    print '\nwelcom to game of guessing! '
    print '===================================\n'
    n_exp = input('Write Number of games :')
    n_rounds = input('write number of rounds per game: ')
    seed = int(raw_input('write seed'))
    random.seed(seed)
    results = play(n_exp, n_rounds)
    print  '---------------------------------------------'
    print 'Machine wins       Player wins         Draw'
    print '    ', results['Machine'], '                 ',results['Player'], '              ',results['Draw']

if __name__ == '__main__':
    sample_run()
