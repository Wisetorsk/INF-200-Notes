import numpy as np
import random as rng
class Circle:
	def __init__(self, x0, y0, R):
		self.x0 = x0
		self.y0 = y0
		self.R = R
		
	def area(self):
		return np.pi*self.R**2
		
	def circumference(self):
		return 2*np.pi*self.R
		
		
class Y:
	def __init__(self, v0):
		self.v0 = v0
		self.g = 9.81
		
	# def value(self, t):
		# return self.v0*t - 0.5*self.g*t**2
		
	def __call__(self, t):
		return  self.v0*t - 0.5*self.g*t**2
		

class Derivative:
	def __init__(self, f, h=1E-5):
		self.f = f
		self.h = float(h)
		
	def __call__(self, x):
		f, h = self.f, self.h 
		return (f(x+h) - f(x))/h
		
		
# Automagic integration

def trapezoidal(f, a, x, n):
	h = (x-a)/float(n)
	I = 0.5*f(a)
	for i in iseq(1, n-1):
		I += f(a + i*h)
	I += 0.5*f(x)
	I *= h
	return I
	
class Polynomial:
	def __init__(self, coeficcients):
		self.coeff = coeffixients 