import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
MAUNA_LOA_CO2_DATA = 'MaunaLoa_CO2_20120305.txt'

def read_data(filename):
	"""Returns dict entry per colmn"""
	raw_data = np.loadtxt(filename, comments = '#')
	complete_years = extract_complete_years(raw_data)
	return {'years':complete_years[:,0],
			'months':complete_years[:, 1],
			'decyears':complete_years[:, 2],
			'co2':complete_years[:, 3],
			'co2_interp':complete_years[:, 4],
			'co2_trend':complete_years[:, 5], 
			'num_no_data':complete_years[:, 6]}
	
def extract_complete_years(raw_data):
	"""Returns data for complete years only"""
	# Find 1st. month and 12th month in dict entry
	jan = 0
	while raw_data[jan, 1] != 1:
		jan += 1
	dec = -1
	while raw_data[dec, 1] != 12:
		dec -= 1
	if dec < -1:
		return raw_data[jan:(dec+1), :]
	else:
		return raw_data[jan:, :]
	
def annual_mean_co2(data):
	"""Returns annual mean co2 const. and years"""
	years = data['years'][::12] # Evaluates entire 'Years' with 12 val step
	n_years = len(years)
	means = np.mean(data['co2_interp'].reshape(n_years, 12), axis = 1)
	return means, years
	
def annual_mean_co2_change(data):
	"""Returns annual change in mean co2 const. and year"""
	means, years = annual_mean_co2(data)
	return means[1:] - means[:-1], years[1:]

def plot_co2(data):
	"""Plots monthly mean co2 data vs time"""
	plt.plot(data['decyears'], data['co2_interp'], 'r-', label = 'Interpolated value')
	plt.plot(data['decyears'], data['co2_trend'], 'b-', label = 'CO2 Trend')
	plt.grid()
	plt.legend()
	plt.xlim(data['years'][0], data['years'][-1])
	plt.xlabel('Years')
	plt.ylabel('CO2 value ppm')
	plt.title('CO2 ppm Muna Loa')
	plt.draw()
	
def plot_co2_change(data):
	"""Plots change in co2 values"""
	delta, years = annual_mean_co2_change(data)
	plt.plot(years, delta, 'b*')
	
def run_analysis(filename):
	data = read_data(filename)
	plt.figure()
	plot_co2(data)
	plt.figure()
	plot_co2_change(data)
	
	
if __name__ == '__main__':
	run_analysis(MAUNA_LOA_CO2_DATA)
	plt.show()