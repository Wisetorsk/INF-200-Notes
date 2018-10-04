import sys, shelve

def setup_databases():
	start_no = shelve.open('data_block.dat')
	start_no['kvitt'] = 0
	start_no['user'] = 0
	start_no.close()

if __name__ == '__main__':
	setup_databases()