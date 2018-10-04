import time, sys, shelve

class Bank:
	
	def __init__(self, name):
		self.data = {'action':['Deposit', 'Withdraw'], 'value':[500, -250]}
		filename = 'data_'+name+'.dat'
		self.balance = shelve.open(filename)
		if len(self.balance) == 0:
			self.balance['balance'] = 00.00
		self.reciet = shelve.open('reciet_log.dat')
		self.name = shelve.open('name.dat')
		if len(self.name) == 0:
			self.name['name'] = None
		if len(self.reciet) == 0:
			self.reciet['no'] = 0

	def timestamp(self):
		hour = str(time.localtime()[3])
		if len(hour) == 1:
			hour = '0' + hour
		minute = str(time.localtime()[4])
		if len(minute) == 1:
			minute = '0' + minute
		second = str(time.localtime()[5])
		if len(second) == 1:
			second = '0'+ second
		timestamp = hour +':'+ minute +':'+ second
		return timestamp	
	
	def datestamp(self):
		day = str(time.localtime()[2])
		if len(day) == 1:
			day = '0' + day
		month = str(time.localtime()[1])
			month = '0' + month
		if len(month) == 1:
		year = str(time.localtime()[0])
		return (day + '/' + month + '/' + year)
	
	def reciept_no(self):
		field_width = 10
		self.reciet['no'] += 1
		out = '0'*(field_width - len(self.reciet)) + str(self.reciet['no'])
		return out
		
	def printout(self):
		print 27*'-' + ' BANK ' + 27*'-'
		print '%10s' % self.reciept_no() + 25*' ' + '%10s' % self.datestamp() + 5*' ' + '%8s' % self.timestamp()
		print '\n\n'
		for a in range(len(self.data['action'])):
			print '%-10s%50s' % (self.data['action'][a], self.data['value'][a])
		print 60*'='
		print 'Balance:%52s' % self.balance['balance']
		print 
		
		if self.name['name'] == None:
			bank_name = '<BANK_NAME>'
		else:
			bank_name = self.name

		if len(bank_name)/2.0 == len(bank_name)/2:
			print (20-len(bank_name)/2)*' '+'Thank you for using %s!' % bank_name +(20-len(bank_name)/2)*' '
		else:
			leng = len(bank_name) + 1
			print (20-(leng/2))*' ' + 'Thank you for using %s!' % bank_name + (20-(leng/2))*' '
		
		print 60*'-'
			
	def end(self):
		self.reciet.close()
		self.name.close()
		self.balance.close()
		
def run():
	Username = Bank(raw_input('Name: ').upper())
	Username.printout()
	Username.end()