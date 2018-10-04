from Tkinter import *
from math import sin, sqrt, exp, cos, tan, atan, asin, acos, pi
from numpy import linspace
import matplotlib
import pylab

def remove_spaces(str):
    out = ''
    for a in str.split(' '):
        out += a
    return out

def GUI(function):
	root = Tk()
	function_entry = Entry(root, width = 20)
	function_entry.pack(side = 'left')
	function_label = Label(root, text = 'Expression involving x')
	function_label.pack(side = 'left')
	
def excecute_comm():
	root.mainloop
	
def plotting_function():
    """This is a function used to plot mathematical functions"""
    
    while True:
        try:
            while True:
                expression = remove_spaces(raw_input('Expression involving x: '))
                if len(expression) == 0:
                    print '!Input Error!\nPlease enter a valid expression!\n'
                else:
                    if 'x' not in expression:
                        print '"x" is not present in expression!\n'
                    else:
                        break
                        
            exp_print = 'F(x) = '+ expression
            
            if 'sqrt(x)' in expression:
                print '\n"SQRT(x)" PRESENT IN EXPRESSION!\nUse caution to ensure that x is not negative!\n'
                
                while True:
                    try:
                        n = int(raw_input('Number of x values: '))
                        break
                    except ValueError:
                        print 'Input error!'
                    except SyntaxError:
                        print 'Input error!'
                        
                while True:
                    try:
                        start = float(raw_input('Starting value: '))
                        if start < 0:
                            print 'Error, current start value is negative and will cause math error!\n'
                        else:
                            break
                    except SyntaxError:
                        print 'Input error!'
                    except ValueError:
                        print 'Input error!'
                        
                while True:
                    try:
                        end = float(raw_input('End value: '))
                        if end < 0:
                            print 'Error, current end value is negative and will cause math error!\n'
                        else:
                            break
                    except SyntaxError:
                        print 'Input error!'
                    except ValueError:
                        print 'Input error!'
                        
                a = linspace(start, end, n)
                y = [eval(expression) for x in a]
                break
                
            elif 'sqrt(' in expression:
                print '\n"SQRT("n"/"function")" PRESENT IN EQUATION!\nPlease ensure that n is nonnegative!'
                n = input('Number of x values: ')
                start = input('Starting value: ')
                end = input('End value: ')
                a = linspace(start, end, n)
                y = [eval(expression) for x in a]
                break
                
            else:
                n = input('Number of x values: ')
                start = input('Starting value: ')
                end = input('End value: ')
                a = linspace(start, end, n)
                y = [eval(expression) for x in a]
                break
                
        except ValueError:
            print 'VALUE ERROR: Possible math domain error in expression?\n'
            
            
    pylab.plot(a,y, label = 'F(x)')
    pylab.xlabel('x')
    pylab.ylabel('y')
    pylab.xlim(start, end)
    pylab.grid()
    pylab.title(exp_print)
    pylab.legend()
    pylab.show()

if __name__ == '__main__':
	
	plotting_function()
