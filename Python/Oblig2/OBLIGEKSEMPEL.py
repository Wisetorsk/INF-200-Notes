# OBLIG EKSEMPEL!!!

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def extract_data(filename):
	juledata = np.loadtxt(filename, comments = '#')
	return {'years': juledata[:,1], 
	'meantemp':juledata[:,2], 
	'mintemp':juledata[:,3],
	'maxtemp':juledata[:,4]}
	
def plot_data(data):
	"""Plots temperatures (mean, min, max)"""
	plt.plot(data['years'], data['mintemp'], 'b-', label = 'Min')
	plt.plot(data['years'], data['meantemp'], 'r-', label = 'Mean')
	plt.plot(data['years'], data['maxtemp'], 'g-', label = 'Max')
	plt.grid()
	plt.xlabel('Years')
	plt.ylabel('Temperature')
	plt.title('Temperature over n years')
	plt.legend()
	plt.draw()
	

	
	
if __name__ == '__main__':
    filename = 'juledata.dat'
    data = extract_data(filename)
    plot_data(data)
    plt.show()
	
	
	
