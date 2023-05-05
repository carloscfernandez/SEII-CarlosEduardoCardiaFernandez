import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

x=np.linspace(0, 10, 10)
y= x**2 *np.sin(x)
plt.scatter(x,y)

from spicy.interpolate import interpid

f=interpid(x,y, kind='linear')
x_dense=np.linspace(0,10,100)
y_dense=f(x_dense)
