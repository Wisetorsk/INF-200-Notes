import os
import sys, shelve

Session = []

# start_number = DATABASEEEEEEEEEEEE
# Users = {}

def register_user(start_number):
    start_number += 1
    id_number = '0' * (8 - len(str(start_number))) + str(start_number)
    Users = enter_empty(id_number)
    try:
        Users[id_number]['ID']['Name'] = raw_input('Enter your full name (First, last name): ')
        os.system('cls')
        Users[id_number]['ID']['Address'] = raw_input('Enter your address: ')
        os.system('cls')
        Users[id_number]['ID']['ZIP'] = raw_input('Enter your area code: ')
        os.system('cls')
        Users[id_number]['ID']['Email'] = raw_input('Enter your email address(if none, leave empty: ')
        if len(Users[id_number]['ID']['Email']) < 2:
            Users[id_number]['ID']['Email'] = None
        os.system('cls')
        Users[id_number]['DATA']['History'].append({'First_reg':(datestamp(), timestamp())})
    except ValueError:
        print 'ERROR'
        
    return Users, start_number
    
def enter_empty(no):
    Users[no] = {'ID':{'Name':None, 'Address':None, 'ZIP':None, 'Email':None}, 'DATA':{'Balance':0.00, 'History':[]}}
    return Users

def timestamp():
    import time
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
	
def datestamp():
    import time
    day = str(time.localtime()[2])
    if len(day) == 1:
        day = '0' + day
    month = str(time.localtime()[1])
    if len(month) == 1:
        month = '0' + month
    year = str(time.localtime()[0])
    return (day + '/' + month + '/' + year)
	
def deposit(Users, id_no):
    while True:
        try:
            amount = float(raw_input('Please enter amount to deposit: '))
            if len(str(amount)) == 0:
                print 'Invalid amount'
            else:
                Users[id_no]['DATA']['Balance'] += amount
                Users[id_no]['DATA']['History'].append({'Deposit': amount, 'Date/time':(datestamp(),timestamp())})
				session.append(['Deposit', amount])
                break
        except ValueError:
            print 'Entry error'
    return Users


def withdraw(Users, id_no):
    while True:
        try:
            amount = float(raw_input('Please enter amount to withdraw: '))
            if len(str(amount)) == 0:
                print 'Invalid amount'
            else:
                if (Users[id_no]['DATA']['Balance'] - amount) < 0:
                    print 'Requested amount exceeds current balance!'
                else:
                    Users[id_no]['DATA']['Balance'] -= amount
                    Users[id_no]['DATA']['History'].append({'Withdraw': -amount, 'Date/time':(datestamp(),timestamp())})
                    session.append(['Withdraw', amount])
					break
        except ValueError:
            print 'Input Error'
    return Users

def reciept_print(session, id_no, reciept_no, Users):
	id_no = str(id_no)
	reciept_no += 1
	print 15*'-' + ' GLOBAL BANKING LTD ' + 15*'-'+'\n'
	print 'Kvitt no. '+'0'*(8 - len(str(reciept_no))) + str(reciept_no) + 13*' ' + datestamp()+ ' ' + timestamp()+'\n'
	for a in range(len(session)):
		print '%s            %30.2f' % (session[a][0], session[a][1])
	print 50*'='
	print 'Current balance: %40.2f' % Users[id_no]['DATA']['Balance']

def enter_command():
    cmd = raw_input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd	

def print_help():
	print 'The available commands are:'
	
	
def main():
	Users = shelve.open('bank_database.dat')
	start = shelve.open('data_block.dat')
	start_no = start['user']
	start_kvitt = start['kvitt']
	try:
		while True:
			cmd = enter_command()
			if cmd == 'register':
				register_user(start_no)
			elif cmd == '?':
				print_help()
	finally Users.close()
	
if __name__ == '__main__':
	# Users, start_number = register_user(start_number)
	main()
	
	
	
	
	
	
# test_hist = [['Deposit ', 500],['Deposit ', 250],['Withdraw', -100]]
reciept_no = 5


	
test_print(test_hist, 1, reciept_no)