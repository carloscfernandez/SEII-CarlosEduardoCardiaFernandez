import numpy as np

a=np.array([[7,8,9,10,11,12,13],[17,18,19,20,21,22,23]])
print(a)
print(a.sim(axis=1))
print(a.mean(axis=1))
print(a.var(axis=1))
print(a.std(axis=1))
print(a.min(axis=1))
print(a.max(axis=1))
