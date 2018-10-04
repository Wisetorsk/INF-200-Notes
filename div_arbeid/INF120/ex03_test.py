# -*- coding: utf-8 -*-

"""
File statistics script
"""


__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


def char_counts(filename):
	result = []
	byte_values = []
	file_a = open(filename, 'rb')
	for line in file_a:
		for letter in line:
			byte_values.append(ord(letter))
#	byte_values = [ord(a) for a in line for line in open(filename, 'rb').split()]
	for value in range(256):
		result.append(byte_values.count(value))
	return result
	
if __name__ == '__main__':

    fname = 'file_stats.py'
    freqs = char_counts(fname)
    for code in range(256):
        if freqs[code] > 0:
            print('{:3}{:10}'.format(code, freqs[code]))
			
	raw_input('End')