# -*- coding: utf-8 -*-

import sys, shelve 

class Timeliste:
	def __init__(self, navn):
		
		filename = 'timeliste '+str(navn).lower().strip() + '.dat'
		self.data = shelve.open(filename)
		
	def hours_input(self):
		while True:
			try:
				week = raw_input('Uke: ')
				day = raw_input('Dag (man, tir, ons, tor, fre, lør): ')
				day_start = float(raw_input('Start: '))
				day_end = float(raw_input('End: '))
				hours = (24 - day_start) - (24 - day_end)
				
				if day == 'lør':
					Ub3 = 18 - day_end
					Ub3 = -Ub3
					if Ub3 < 0:
						Ub3 = 0
				else:
					Ub3 = 0
					if day_end >= 23:
						Ub2 = 21-day_end
						Ub2 = - Ub2
						if Ub2 < 0:
							Ub2 = 0
						else:
							Ub2 = 0
					else: 
						Ub2 = 0
						
					if day_end > 18:
						Ub1 = (18 - day_end) - (21-day_end)
						Ub1 = - Ub1
						if Ub1 < 0:
							Ub1 = 0
					else:
						Ub1 = 0
				if day_end > 18:
					norm = day_start - 18
				else:
					norm = hours
				
				self.data[week][day] = [hours, Ub1, Ub2, Ub3, norm]
				quit = raw_input('Quit entry? ("y/n"): ')
				if quit.strip().lower() == 'y':
					break
			except ValueError:
				print 'Input Error'
		print self.data
	
	def print_hours(self):
		for a in self.data:
			print 'Uke: %s\n' % a
			for b in self.data[a]:
				if b[0] == 'man':
					dag = 'Mandag'
				elif b[0] == 'tir':
					dag = 'Tirsdag'
				elif b[0] == 'ons':
					dag = 'Onsdag'
				elif b[0] == 'tor':
					dag = 'Torsdag'
				elif b[0] == 'fre':
					dag = 'Fredag'
				elif b[0] == 'lør':
					dag = 'Lørdag'
				print 'Dag: %s\nTotal: %.2s Timer.    UB1: %.2s Timer.    UB2: %.2s Timer.    UB3: %.2s Timer.' % (dag, b[1], b[2], b[3], b[4])

	def pay_calc(self):
		payout = {}
		for a in self.data:
			Ukesum = 0
			payout[a] = []
			for b in self.data[a]:
				Ukesum += b[1]
			if Ukesum >= 20:
				for x in self.data[a]:
					dag_pay = (x[2] * (151 + 21)) + (x[3] * (151 + 42)) + (x[4] * (151 + 84))
					payout['a'].append([x[0], dag_pay])
			else: 
				for x in self.data[a]:
					dag_pay = x[1] * 151
					payout['a'].append([x[0], dag_pay])
		self.payout = payout

	def print_pay(self):
		
		for a in self.payout:
			print 'Uke %.2s' % a
			for b in a:
				print 'Dag: %s    Lønn: %4.2f    Etter skatt: %4.2f' % (b[0], b[1], b[1]*0.79)
				
	def print_total(self):
		
		tot = 0
		for a in self.payout:
			for b in a:
				tot += b[1]
		tot_tax = tot * 0.79
		print 'Total amount earned befor tax: %5.2f\nAfter tax: %5.2f' % (tot, tot_tax)

def print_help():
	print 'Mulige kommandoer:\n"Registrer" - Registrer timer\n"Timer" - Printer dine registrerte timer \n"Dagslønn" - Printer lønn per dag \n"Total" - Printer total akkumulert lønn'
		
def run():
	inst = Timeliste(raw_input('Navn: '))
	
	while True:
		valg = select()
		if valg == '?':
			print_help()
		elif valg == 'registrer':
			inst.hours_input()
		elif valg == 'timer':
			
			inst.print_hours()
		elif valg == 'dagslønn':
			inst.pay_calc()
			inst.print_pay()
		elif valg == 'total':
			inst.pay_calc()
			inst.print_total()

def select():
	selection = raw_input('Valg ? for hjelp: ')
	return selection.strip().lower()

	
if __name__ == '__main__':
	run()