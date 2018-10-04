
class Account:
	def __init__(self, balance, name, acc_no):
		self._balance = balance
		self._name = name 
		self._no = acc_no
	
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
		print "Welcome to 'GLOBAL Banking ATM'"
	


	
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

"""
class Person:
	def __init__(self, name, 
				mobile_phone = None,
				office_phone = None,
				private_phone = None,
				email = None):
		self.name = name
		self.mobile = mobile_phone
		self.office = office_phone
		self.private = private_phone
		self.email = email
		
	def add_mobile_phone(self, number):
		self.mobile = number
		
	def add_office_phone(self, number):
		self.office = number
		
	def add_private_phone(self, number):
		self.private = number
		
	def add_email(self, address):
		self.email = address
	
	def dump(self):
		s = self.name + '\n'
		if self.mobile is not None:
			s += 'mobile phone: %s\n' % self.mobile
		if self.office is not None:
			s += 'office phone: %s\n' % self.office
		if self.private is not None:
			s += 'private phone: %s\n' % self.private
		if self.email is not None:
			s += 'email: %s\n' % self.email
		print s
		
		
if __name__ == "__main__":
	# banking()
	p1 = Person("Erna Solberg", office_phone = 12345678) # Setter opp instans nr.1 av Perosons
	p2 = Person("Siv Jensen", email="SivJensen@retard.no") # Setter opp instans nr.2 av Persons
	p1.add_email("Erna@feitku.no")
	p2.add_mobile_phone(32154684)
	phone_book = [p1, p2]
	for person in phone_book:
		person.dump() # Skriver ut info i begge instansene (p1 og p2)
"""