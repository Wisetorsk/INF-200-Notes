import sys, shelve

def register_product(ean, db):
	navn = raw_input('Varenavn: ')
	pris = float(raw_input('Enhetspris: '))
	ne_vekt = float(raw_input('Nettovekt: '))
	br_vekt = float(raw_input('Bruttovekt: '))
	produsent = raw_input('Produsent: ')
	type = raw_input('Varetype: ')
	data = raw_input('Tileggsinfo (La stå tom, hvis ingen): ')
	if len(data) <= 1:
		data = None
	kr_kg = (float(pris)/br_vekt) * 100
	
	db[ean] = {'VARENAVN':navn.lower().strip().capitalize(), 'PRIS':pris, 'NETTOVEKT':ne_vekt, 'BRUTTOVEKT':br_vekt, 'PRODUSENT':produsent.lower().strip().capitalize(), 'VARETYPE':type.lower().strip().capitalize(), 'DATA':data, 'Kr/Kg':kr_kg}

def display_product(ean, db):
	for a in db[ean]:
		if isinstance(db[ean][a], float) is True:
			print '%-15s: %30.2f' % (a, db[ean][a])
		elif isinstance(db[ean][a], int) is True:
			print '%-15s: %30.2f' % (a, db[eab][a])
		else:
			print '%-15s: %30s' % (a, db[ean][a])

def main():
	while True:
		register_product(raw_input('Produkt EAN: '), db)
		nytt = raw_input('Registrer nytt produkt ("j"/"n")?: ')
		if nytt == "n":
			break

db = shelve.open('ean_dbase.dat')
main()
display_product(raw_input('EAN: '), db)
db.close()