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
    mean_RH = [(sum(hourly_rh[a:a+12])/12) for a in range(0, len(hourly_rh)+1, 12)]
    del mean_RH[len(mean_RH) - 1]
    mean_TS = [(sum(hourly_temp[a:a+12])/12) for a in range(0, len(hourly_temp)+1, 12)]
    del mean_TS[len(mean_TS) - 1]
    data = [mean_TS, mean_RH]    
    return np.array(data)

def compute_dose(temp, rh, n = 730):
    """
    Computes doses : Dose Rh, dose temperature and total dose.
    """
    Dtotlist = []
    for a in range(n):

        if rh[a] > 75:
            Drh = 0.5*np.exp(15.5*np.log(rh[a]/90.0))
        elif 60 < rh < 75:
            Drh = -2.118 + 0.0286 * rh[a]
        elif rh[a] < 60:
            Drh = -0.4
    
        if temp[a] > 29:
            Dt = 1.0
        elif temp[a] > 0.1:
            Dt = np.exp(2.0*np.log(temp/20.0))
    		
    	
        if rh[a] > 75:
            if temp[a] > 0.1:
                Dtot = Drh * Dt
            else:
                Dtot = -0.4
        elif 60 < rh[a] < 75:
            Dtot = Drh
        elif rh[a] < 60:
            Dtot = -0.4
        Dtotlist.append(Dtot)
    return np.array(Dtotlist)
		
                    
def compute_mould(Dtot, n = 730, Dcrit = 10):
    """
    Compute the cumulated mould
    """
    
	
    return mould

    

def plot_mould(mnorth, msouth):
    """
    Plot the mould on the north and south side
    """
    plt.title('Mould growth')
    plt.subplot(2,1,1)
    plt.plot(val1, val2, 'r-', label= 'Kurvelabel 1')
    plt.grid()
    plt.xlabel('Label')
    plt.ylabel('Label')
    plt.legend()
    plt.subplot(2,1,2)
    plt.plot(val3, val4, 'b-', label= 'Kurvelabel 2')
    plt.grid()
    plt.xlabel('Label')
    plt.ylabel('Label')

    plt.legend()




def run_analysis(northf,southf):
    """
    Performs complete analysis, including
        - reading data from file
        - computing doses
        - computing the mould
        - plotting the mould
    """
    data = read_data(northf, southf)
    mean_north = mean12h_values(data['TempSurface_north'], data['RHsurface_north']) # Mean values
    mean_south = mean12h_values(data['TempSurface_south'], data['RHsurface_south']) # Mean values

    Dtot_north = compute_dose(mean_north[0], mean_north[1]) # Dose
    Dtot_south = compute_dose(mean_south[0], mean_south[1]) # Dose
    mould_north = compute_mould(Dtot_north)
    mould_south = compute_mould(Dtot_south)
    plot_mould(mould_north, mould_south)
	

    


if __name__ == "__main__":
    northf = 'North.asc'
    southf = 'South.asc'
    run_analysis(northf, southf)
    plt.show()