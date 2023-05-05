import numpy as np

a = np.array([[1,2,3,4]])
#a = np.array([[1,2],[3,4]])
print(a)
b=np.array([[5,6,7,8]])
#b=np.array([[5,6]])
#c=np.hstack((a,b))
c=np.vstack((a,b))
#c=np.concatenate((a,b.T),axis=1)
print(c)
