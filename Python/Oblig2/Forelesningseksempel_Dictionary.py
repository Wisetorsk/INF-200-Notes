# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:22:04 2015

@author: Marius
"""

# Lesing av str-fil

import numpy as np

infile = open('MyFile.txt', 'r')
lines = infile.readlines()
infile.close()

mean = 0
for number in lines:
    number = float(number)    
    mean += number
mean_val = mean/len(lines)
print mean_val



infile = open('rainfall.txt', 'r')
infile.readline()
numbers = []
for line in infile:
    words = line.split()
    number = float(words[1])
    numbers.append(number)
infile.close()

print numbers

import matplotlib.pyplot as plt
months = range(1, 13)
plt.plot(months, numbers[:-1], 'ro')
plt.grid()
plt.xlabel('Months')
plt.ylabel('Rainfall')
plt.title('Rainfall in Rome')