# Users = {'USER1':HASH, 'USER2':HASH}
import time
import webbrowser as web
import sys, shelve

class Security:

	def __init__(self, databasename):
		databasename = databasename+'.dat'
		self.db = shelve.open(databasename)
	
	def register_user(self, db):
		self.create_hash(password)
		
	def create_hash(self, input):
		return hash
		
	def recognize_and_handshake(self):
		self.create_hash(password_user.get)
		pass
	
	def control_hash(self):
		
	
	def let_through(self):
		pass
		
def home():
	pass 
	
def run():
	basename = Security(raw_input('Enter database name'))
	
if __name__ == '__main__':
	run()