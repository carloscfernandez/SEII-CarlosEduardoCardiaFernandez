import numpy as np


a = np.arrange(1,7)
print(a)
print(a.shape)
#b=a.reshape((3,2))
#print(b)

b=a[np.newaxis, :]
print(b.shape)
