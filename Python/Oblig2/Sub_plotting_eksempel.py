import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def f(t):
	return t**2*np.exp(-t**2)

def g(t):
	return t**2*f(t)
	
t = np.linspace(0,3,51)
plt.figure()
plt.subplot(2,1,1)
plt.plot(t, f(t), '-r')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Top Figure')
plt.grid()

plt.subplot(2,1,2)
plt.plot(t, g(t), 'bo')
plt.xlabel('t')
plt.ylabel('g(t)')
plt.axis([0,4,0,0.6])
plt.title('Bottom Figure')
plt.grid()
plt.savefig('testplot.pdf')
plt.show()
