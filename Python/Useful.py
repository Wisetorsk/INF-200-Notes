import os
import time

def clear():
	os.system('cls')
	
def wait(seconds):
	clear()
	for a in range(seconds):
		print 'Please wait' + (seconds - a) * '.'
		time.sleep(1)
		clear()
		
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
	if len(month) == 1:
		month = '0' + month
	year = str(time.localtime()[0])
	return (day + '/' + month + '/' + year)