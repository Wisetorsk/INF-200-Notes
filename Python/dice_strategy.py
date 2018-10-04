import random
import sys

def roll_dice_and_compute_sum(ndice):
    return sum([random.randint(1, 6) for i in range(ndice)])

def computer_guess(ndice):
    return random.randint(ndice, 6*ndice)

def player_guess(ndice):
    return 12

def play_one_round(ndice, capital, guess_function):
    guess = guess_function(ndice)
    throw = roll_dice_and_compute_sum(ndice)
    if guess == throw:
        capital += guess
    else:
        capital -= 1
    return capital, throw, guess

def play(ngames,nrounds, ndice=2):
    wins = {'Machine': 0, 'You': 0, 'D': 0}
    for i in xrange(ngames):
        player_capital = computer_capital = nrounds  # start capital
        for j in range(nrounds):
            player_capital, throw, guess = \
                 play_one_round(ndice, player_capital, player_guess)

            computer_capital, throw, guess = \
                play_one_round(ndice, computer_capital, computer_guess)

        if computer_capital > player_capital:
            winner = 'Machine'
        elif computer_capital < player_capital:
            winner = 'You'
        else: 
            winner = 'D'
        wins[winner] += 1
    return wins

def sample_run():
    print '\nWelcome to game of guessing !'
    print '==============================\n'
    n_exp = int(raw_input('Number of games per strategy combination: '))
    n_rounds = int(raw_input('Number of rounds per game: '))
    seed = int(raw_input('random generator seed: '))
    random.seed(seed)
    
    results = play(n_exp, n_rounds)
    print '---------------------------'
    print 'Machine wins     You wins        Draw'
    print '   ',results['Machine'],'           ',results['You'],'            ',results['D']
    print

            
if __name__ == '__main__':
    sample_run()
