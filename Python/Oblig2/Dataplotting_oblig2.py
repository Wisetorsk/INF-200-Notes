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


import matplotlib.pyplot as plt
import numpy as np

data = read_data('north.asc', 'south.asc')
plt.subplot(2,1,1)
plt.plot(data['Hours'],data['TempSurface_north'], 'r-', label = 'North')
plt.plot(data['Hours'],data['TempSurface_south'], 'b-', label = 'South')
plt.grid()
plt.xlabel('Hours')
plt.ylabel('Temperature')
plt.title('Surface Temp')
plt.legend()

plt.subplot(2,1,2)
plt.plot(data['Hours'],data['RHsurface_south'], 'r-', label = 'South')
plt.plot(data['Hours'],data['RHsurface_north'], 'b-', label = 'North')
plt.grid()
plt.xlabel('Hours')
plt.ylabel('Humidity')
plt.title('Relative Humidity')
plt.legend()
plt.savefig('Data.png')
plt.show()