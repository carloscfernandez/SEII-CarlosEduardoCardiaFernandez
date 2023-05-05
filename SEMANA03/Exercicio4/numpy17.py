import numpy as np

A=np.array([[1,1],[1.5,4.0]])
b=np.array([2200,5050])

#X=np.linalg.inv(A).dot(b)
print(X)

x=np.linalg.solve(A,b)
print(x)
