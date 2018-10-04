# Test oblig

import numpy as np
import matplotlib.pyplot as plt


###########################################
def Drh(RHsurface):
	if RHsurface > 75:
		Drh = 0.5*np.exp(15.5*log(RHsurface/90.0))
	elif 60 < RHsurface < 75:
		Drh = -2.118 + 0.0286 * RHsurface
	elif RHsurface < 60:
		Drh = -0.4
	return Drh

def Dt(TempSurface):
	if TempSurface > 29:
		Dt = 1.0
	elif TempSurface > 0.1:
		Dt = np.exp(2.0*log(TempSurface/20.0))
	return Dt
	
def Dtot(RHsurface, TempSurface):
	if RHsurface > 75:
		if TempSurface > 0.1:
			Dtot = Drh * Dt
		else:
			Dtot = -0.4
	elif 60 < RHsurface < 75:
		Dtot = Dr*h
	elif RHsurface < 60:
		Dtot = -0.4
	return Dtot

def S_index(Dtot, Dcrit):
	return Dtot/Dcrit
############################################	
	
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

	
	
data = read_data('north.asc', 'south.asc')

TS = data['TempSurface_north']
mean_TS = []
for a in range(0, len(TS)+1, 12):
	b = a+12
	mean_TS.append(sum(TS[a:b])/12)
del mean_TS[len(mean_TS) - 1]
mean_TS = np.array(mean_TS)	

RH = data['RHsurface_north']
mean_RH = []
for a in range(0, len(RH)+1, 12):
	b = a+12
	mean_RH.append(sum(RH[a:b])/12)
del mean_RH[len(mean_RH) - 1]
mean_RH = np.array(mean_RH)


