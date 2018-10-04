
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:35:22 2015
 
@author: montyhatfield
"""
import random
 
 
def one_round(total, strategi):
    if strategi == 'six':
        total = terminate_six(total)
    else:
        total = terminate_sub_tot_13(total)
		
    return total
     
     
         
def one_game(strategi_a, strategi_b, game_tot_b = 0, game_tot_a = 0): # Noen småendringer
    while True:
        if game_tot_a >= 63:
            break
        elif game_tot_b >= 63:
            break
        else:
             game_tot_a = one_round(game_tot_a, strategi_a)
             game_tot_b = one_round(game_tot_b, strategi_b)        
    # if game_tot_a == game_tot_b:
        # print game_tot_a, game_tot_b          
    if game_tot_a > game_tot_b:
        return 'A'
    elif game_tot_b > game_tot_a:
        return 'B'
    else:
        return 'D'
 
 
def play_games(n_games):
    wins_6_6 = {'A' :0, 'B' :0, 'D' :0}
    wins_6_13 = {'A' :0, 'B' :0, 'D' :0}
    wins_13_6 = {'A' :0, 'B' :0, 'D' :0}
    wins_13_13 = {'A' :0, 'B' :0, 'D' :0}
    for _ in range(n_games):
        wins_6_6[one_game('six', 'six')] += 1
         
        wins_6_13[one_game('six', 'thirteen')] += 1
         
        wins_13_6[one_game('thirteen', 'six')] += 1
        
        wins_13_13[one_game('thirteen', 'thirteen')] += 1
    return wins_6_6, wins_6_13, wins_13_6, wins_13_13
 
     
 
def terminate_six(total): # HER HAR JEG ENDRET LITT
    sub_tot = 0
    while True:
            di = random.randint(1, 6)
            if di == 1:
                total = 0   
                break
				 
            elif di == 6:
                total = total + sub_tot + 6
                break
				 
            else:
                sub_tot += di
             
            if (total + sub_tot) >= 63:
				total += sub_tot
				break
				
    return total
 
 
def terminate_sub_tot_13(total): # Det er lurt å kun a en instans av "return" per funksjon
    sub_tot = 0
    while sub_tot < 13:
            di = random.randint(1, 6)
            if di == 1:
                return total
         
            elif (total + sub_tot + di) > 63:
                return total + sub_tot + di
             
            else:
                sub_tot = sub_tot + di
                 
         
    return total + sub_tot
  
 
 
def sample_run():
    print '\nWelcom to game 13-6! '
    print '===================================\n'
    n_exp = input('Write Number of games : ')
    seed = int(raw_input('write seed : '))
    random.seed(seed)
    S_S, S_T, T_S, T_T = play_games(n_exp)
    print ''
    print  '---------------------------------------------------------------------------------'
    print 'Strategy A          Strategy B           A wins              B wins         Draw'
    print  '---------------------------------------------------------------------------------'
    print 'Stop on 6           Stop on 6             ',S_S['A'],'                 ',S_S['B'],'             ' ,S_S['D']
    print 'Stop on 6           Stop on sum 13        ',S_T['A'],'                 ',S_T['B'],'             ' ,S_T['D']
    print 'Stop on sum 13      Stop on 6             ',T_S['A'],'                 ',T_S['B'],'             ' ,T_S['D']
    print 'Stop on sum 13      Stop on sum 13        ',T_T['A'],'                 ',T_T['B'],'             ' ,T_T['D'] 
 
     
if __name__ == '__main__':
    sample_run()
     
       