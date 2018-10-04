'''
Created on Apr 18, 2012

@author: inbu
'''
import random
wordlist = ['hello','how','are','you','the','weather','is','beautiful','nasty']
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

def get_random_word(wordLen):
    word = ''
    for i in range(wordLen):
        word += random.choice(chars)
    return word

def get_random_string(numberwords):
    s = ''
    for i in range(numberwords):
        s += ' ' + random.choice(wordlist)
    return s

if __name__ == '__main__':
    wordLen = random.randint(5, 15)
    print get_random_word(wordLen)
    nowords = random.randint(5,15)
    print get_random_string(nowords)
    raw_input('')