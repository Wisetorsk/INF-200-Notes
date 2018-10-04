'''
Created on Apr 3, 2013

@author: inbu
'''
import numpy as np
N = input('How many experiments ?')
eyes = np.random.randint(1,7,N)
succes = eyes == 6 # true/false array
M = np.sum(succes)

print 'got six %d times out of %d' % (M, N)
probability = float(M)/N
print 'estimated probability getting 6 is ',probability