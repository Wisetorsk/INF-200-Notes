# -*- coding: utf-8 -*-
print 'Dette er en enkel loennskalkulator som ikke tar hensyn til tilegg \nDen tar en skatteprosent paa 21% og basisloenn paa kr 155.9 som utgangspunkt\n\n'
print 'Hvordan skal programmet regne ut antall timer?\n\nHvis du velger "timer", oppgir du totalt antall timer du har jobbet\nProgrammet tar da utgangspunkt i pause paa 0.5 timer per 8 timer jobbet\n\nHvis du velger klokkeslett, maa du oppgi hvor mange dager,\nsamt start og slutttidspunkt paa disse dagene.\n\n\n'
while True:
	try:
		select = raw_input('Vennligst skriv: "timer" eller "Klokkeslett": ')
		if select.strip().lower() == 'timer':
			break
		elif select.strip().lower() == 'klokkeslett':
			break
		else: 
			print 'Input error, vennligst prøv igjen'
	except ValueError:
		print 'ERROR'
if select.strip().lower() == 'timer':
	while True:
		try:
			timer = int(raw_input('Totalt antall timer: '))
			dager = timer/8.0
			dager = int(dager)
			timer = timer - (dager * .5)
			break
		except ValueError:
			print 'Feil under inntasting av antall timer, proev igjen.'
else:
	while True:
		try:
			dag = int(raw_input('Hvor mange dager har du jobbet?: '))
			break
		except ValueError:
			print 'Feil under inntasting av antall dager, proev igjen'
	timer = 0
	for a in range(dag):
		while True:
			try:
				start = float(raw_input('Start dag %s: ' % (a + 1)))
				slutt = float(raw_input('Slutt dag %s: ' % (a + 1)))
				tid = (slutt - start)
				if tid <= 0:
					print 'Feil ved input\nVennligst oppgi STARTtid og SLUTT-tid igjen'
				elif tid > 5.5:
					over = raw_input('Var dere over 2 pers? ("y"/"n"): ')
					if over.strip().lower() == 'y':
						timer += (tid - .5)
						print 'Timer: %3.1f\n' % timer
						break
					else:
						timer += tid
						print 'Timer: %3.1f\n' % timer
						break
				else:
					timer += tid
					print 'Timer: %3.1f\n' % timer
					break
			except ValueError:
				print 'INPUT ERROR'
		
sum = timer * 155.95
while True:
	try:
		skatt = int(raw_input('Skatteprosent: '))
		skatt = float(skatt)/100.0
		sum = sum * (1 - skatt)
		break
	except ValueError:
		print 'Skatteprosent skal skrives inn som enten KUN heltall eller decimaltall "xx"/"xx.xx"'
print '\n\n%3.0f effektive arbeidstimer tilsvarer en omtrentlig sum paa %.2f + tillegg\n' % (timer, sum) + ' ' + '='*58

raw_input('\n'+20*' ' + 'Press <Enter> to close this window')