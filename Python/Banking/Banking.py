import random as rng
import numpy as np

class Account:
	def __init__(self, balance = None, name = None, acc_no = None):
		self._balance = balance
		self._name = name 
		self._no = acc_no
	
	def register_user(self):
		self._name == raw_input('Full name: ')
		_no = np.random.randint(1,10,14)
		out = []
		for a in _no:
			out.append(str(a))
		self._number = ''.join(out)
		print self._number[0:4] + " " + self._number[4:7] + " " + self._number[7:11] + " " + self._number[11:15]
		
	def deposit(self, amount):
		print "-"*50
		print "Account holder: %s" % self._name
		print "Account number: %s" % self._no
		print "-"*50
		print "Deposit\n"
		print "Old balance: %27.2f" % self._balance
		self._balance+= amount
		print "+%39.2f" % amount
		print "="*50
		print 'Your current balance is: %15.2f' % self._balance
		print "="*50
		
	def withdraw(self, amount):
		print "-"*50
		print "Account holder: %s" % self._name
		print "Account number: %s" % self._no
		print "-"*50
		print "Withdrawal\n"
		print "Old balance: %27.2f" % self._balance
		self._balance-= amount
		print "-%39.2f" % amount
		print "="*50
		print 'Your current balance is: %15.2f' % self._balance
		print "="*50
		
	def get_balance(self):
		return self._balance
	
	def dump(self):
		print "-"*50 
		print "Account holder: %s" % self._name
		print "Account number: %s" % self._no
		print "="*50
		print 'Your current balance is: %15.2f' % self._balance
		print "="*50
		
	def start_print(self):
		print "/n/nWelcome to 'GLOBAL Banking LMT'"
	


	
def banking():
	bank = Account(input('Balance: '), raw_input("Name: ").upper(), input("Account Number: "))
	while True:
		bank.start_print()
		selection = raw_input("\n\nDeposit, Withdraw or Balance: ").lower()
		choice = "bank."
		end_0 = "()"
		end_L = "("
		end_R = ")"
		if selection == "balance":
			function = "dump"
			end = end_0
		elif selection == "withdraw":
			function = "withdraw"
			sum = raw_input("Amount: ")
			end = end_L+sum+end_R
		elif selection == "deposit":
			function = "deposit"
			sum = raw_input("Amount: ")
			end = end_L+sum+end_R
		eval(choice+function+end)

