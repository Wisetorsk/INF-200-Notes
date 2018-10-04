# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:22:20 2015

@author: Marius
"""

temps = {'Oslo':13, 'Paris':15, 'London':12}

for city in temps:
    print city, temps[city]
    
if 'Berlin' in temps:
    print temps['Berlin']
else:
    print 'No temp for "Berlin"'



    
p = {0:-1, 2:1, 7:3}

def poly1(data, x):
    sum1 = 0.0
    for power in data:
        sum1 += data[power]*x**power
    return sum1
    
    
rates = {}
rates['USD'] = {}
rates['NOK'] = {}
rates['EUR'] = {}
rates['USD']['EUR'] = 0.75
rates['USD']['NOK'] = 5.72
rates['EUR']['NOK'] = 7.54
rates['NOK']['EUR'] = 1.0/rates['EUR']['NOK']
rates['NOK']['USD'] = 1.0/rates['USD']['NOK']
rates['EUR']['USD'] = 1.0/rates['USD']['EUR']



fromCurrency = raw_input('Currency to be exchanged: ').upper()
toCurrency = raw_input('Currency requested: ').upper()
amount = float(raw_input('Amount to be changed: '))

if fromCurrency not in rates:
    print 'Currency not known'
else:
    conv_amount = amount * rates[fromCurrency][toCurrency]
    print '%.2f %s is %.2f %s' % (amount, fromCurrency, conv_amount, toCurrency)
