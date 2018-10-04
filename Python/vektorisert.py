# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 20:09:55 2014

@author: inbu
"""

import numpy as np
eyes = np.random.randint(1, 7, (100, 5))
compare = eyes == 6
n6 = np.sum(compare, 1)
six_only = n6 >= 2
M = np.sum(six_only)
print M
