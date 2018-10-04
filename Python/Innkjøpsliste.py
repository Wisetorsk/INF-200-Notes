def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


		
def writefile(data, filnavn):
	"""Data in in the form of dictionary. File out as Ecxel spreadsheet"""
	pass
	
def register(ting):
	"""
	This function registers input to a dictionary ("ting") to be stored permanently
	"""
	clear()
	prioriteter = ['Skal skaffes', 'Burde skaffes', 'Uviktig']
	while True:
		try:
			while True:
				try:
					prioritet()
					Ting = raw_input('Ting: ').lower().capitalize()
					if len(Ting) <= 2:
						raise NameError('The specified "thing" does not appear to be a proper word\n')
					else: 
						break
				except NameError:
					print 'The specified "thing" does not appear to be a proper word'
			ting[Ting] = [int(raw_input('Prioritet("1","2" eller "3"): ').strip()), float(eval((raw_input('Verdi (ca.): '))))]
			print 'Ting: %-20s Prioritet: %-20s Verdi: Kr %-15s' % (Ting, prioriteter[ting[Ting][0] - 1], ting[Ting][1])
			end = raw_input('End? ("y"/"n"): ')
			print '\n'
			if end == 'y':
				break
			clear()
		except ValueError:
			print 'Vennligst fyll inn kun INT'

def prioritet():
	"""
	Simple function to simplify printout
	"""
	print 'Prioriteter\n\n1 - Skal skaffes\n2 - Burde skaffes\n3 - Uviktig\n\n'
	
def printout(dict):
	"""
	Prints the content of the data dictionary. If the dictionary is empty, the user will be prompted to store data in it
	"""
	clear()
	prioriteter = ['Skal skaffes', 'Burde skaffes', 'Uviktig']
	if len(dict) < 1:
		print 'Det er ingen registrerte data ennaa'
		reg = raw_input('Registrer? ("y"/"n"): ')
		if reg.lower().strip() == 'y':
			main(default = 1)
	else:
		print '|'+'-'*60 + '|'
		print '|%-20s|    %-10s|    %-20s|' % ('TING', 'PRIS', 'PRIORITET')
		print '|'+'-'*60 +'|'
		for a in dict:
			print '|%-20s|    %-10s|    %-20s|' % (a, dict[a][1], prioriteter[dict[a][0] - 1])
		print '|'+'-'*60 + '|'
		print '|' + 'SUM''%57.2f' % summering(dict) + '|'
		print '|'+'='*60 +'|'
		print '\n'
	while True:
		try:
			export_doc = raw_input('Export as excel file? ("y"/"n"): ').strip().lower()
			if export_doc == 'y':
				writefile(dict, 'Innkjøpsliste')
				break
			else:
				break
		except NameError:
			print 'ERROR!'
def clear():
	"""
	Cleans up the command interface
	"""
	os.system('cls')

def help_me():
	print '\n\nHJELP!\nDette programmet hjelper deg aa holde styr paa hva som trengs \naa kjoepe inn, og hvor viktig det er.\n\nMulige kommandoer er:\n"Registrer" - Starter modulen som gjoer det mulig aa skrive inn produkter, pris og prioritet.\n"Print" - Viser de produktene som er lagret.\n"quit" - Avslutter programmet.\n'

def exit_prog(db):
	"""
	Closes the database and exits the program
	"""
	confirm = raw_input('Press any key to confirm (type abort and press <Enter> to go back): ')
	if confirm.strip().lower() == 'abort':
		main()
	else:
		db.close()
		exit()
		
def summering(db):
	sum = 0
	for a in db:
		sum += db[a][1]
	return sum
	
def main(default = 0):
	"""
	Program core:
	
	Creates a database and executes the scripts's primary functions.
	"""
	ting = shelve.open('LISTE.dat')
	clear()
	while True:
		if default == 1:
			register(ting)
			default = 0
		else:
			choose = raw_input('AVSLUTT PROGRAMMET VED AA SKRIVE "quit"\nRegistrer eller print ( "?"/"hjelp" for hjelp ): ')
			if choose.lower() == 'registrer':
				register(ting)
			elif choose.lower() == '?':
				help_me()
			elif choose.lower() == 'hjelp':
				help_me()
			elif choose.lower() == 'quit':
				exit_prog(ting)
			elif choose.lower() == 'print':
				try:
					printout(ting)
				except NameError:
					print 'You have not registered any data'
					raw_input('Press any key to continue with data input: ')
					register(ting)
				
if __name__ == '__main__':
	import_list = ['xlwt', 'os', 'shelve', 'sys']
	for var in import_list:
		install_and_import(var)
	main()