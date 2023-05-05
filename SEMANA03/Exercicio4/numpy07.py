import numpy as np


a = np.array([10,19,30,41,50,61])
#a = np.array([1,2],[3,4],[5,6])
print(a)
#b=[1,3,5]
#print(a[b])

even=np.argwhere(a%2==0).flatten()
print(a[even])

#bool_idx = a>2
#print(bool_idx)
#print(a(bool_idx)
#print(a[a>2])

#b=np.where(a>2,a,-1)
#print(b)


#print(a[0,0])
#print(a.shape)
#print(np.linalg.det(a))

#b=a[:,0]
#print(b)
