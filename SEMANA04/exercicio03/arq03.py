import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from spicy.optimize import curve_fit

def func(x, a, b):
    return a*x**2 +b

popt, pcov = curve_fit(func, x_data, y_data, p0=(1,1))
popt

def func(x, A, w, phi):
    return A*np.cos(w*t+phi)

t=np.linspce(0,10,100)
y=func(t, A, w, phi)

plt.plot(t,y)
