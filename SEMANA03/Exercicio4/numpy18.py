import numpy as np

#data=np.genfromtxt('teste.csv', delimiter=",",dtype=np.float32)
data=np.loadtxt('teste.csv', delimiter=",",dtype=np.float32)
print(data.shape)
