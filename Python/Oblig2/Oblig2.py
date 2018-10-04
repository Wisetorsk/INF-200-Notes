## -*- coding: utf-8 -*-
"""
Obligatorisk oppgave nr 2 i INF120, Våren 2015.
"""
__author__ = "Marius Kristiansen"
__email__ = "mariukri@nmbu.no"


import numpy as np
import matplotlib.pyplot as plt


def read_data(northf, southf):
	"""Returns data as dictionary"""
	north = np.loadtxt(northf)
	south = np.loadtxt(southf)
	output = {
	'Hours':north[:8760, 0],
	'TempSurface_north':north[:8760, 1],
	'RHsurface_north':north[:8760, 2],
	'TempSurface_south':south[:8760, 1],
	'RHsurface_south':south[:8760, 2],
	}
	return output

	
	
def mean12h_values(hourly_temp, hourly_rh):
	"""
	Returns array of 12 h mean temperature and rh.
	"""
	mean_TS = [(sum(hourly_rh[a:a+12])/12) for a in range(0, len(hourly_rh)+1, 12)]
	del mean_TS[len(mean_TS) - 1]
	mean_TS = np.array(mean_TS)	
	
	mean_RH = [(sum(hourly_temp[a:a+12])/12) for a in range(0, len(hourly_temp)+1, 12)]
	del mean_RH[len(mean_RH) - 1]
	mean_RH = np.array(mean_RH)
	
	return mean_TS, mean_RH
	


def compute_dose(temp, rh, n = 730):
    """
    Computes doses : Dose Rh, dose temperature and total dose.
    """

                    
def compute_mould(Dtot, n = 730, Dcrit = 10):
    """
    Compute the cumulated mould
    """

    

def plot_mould(mnorth, msouth):
    """
    Plot the moul on the north and south side
    """





def run_analysis(northf,southf):
	"""
	Performs complete analysis, including
        - reading data from file
        - computing doses
        - computing the mould
        - plotting the mould
	"""
	data = read_data(northf, southf)
	hourly_temp_north = data['TempSurface_north']
	hourly_temp_south = data['TempSurface_south']
	hourly_rh_north = data['RHsurface_north']
	hourly_rh_south = data['RHsurface_south']
	

    


if __name__ == "__main__":
    northf = 'North.asc'
    southf = 'South.asc'
    run_analysis(northf, southf, westf, eastf)
    plt.show()