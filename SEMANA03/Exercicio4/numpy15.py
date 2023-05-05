import numpy as np

a=np.random.random((3,2))   #aleatorios entre 0 e 1
print(a)

a=np.random.randn((1000))   #distribuição normal ou gaussiana
print(a.mean(),a.var())

a=np.random.randint(3,10,sizze=(3,3))
print(a)

a=np.random.choice(-8,-7,-6,size=10)
print(a)
