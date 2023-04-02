import numpy as np

x = range(20)
y = range(20)

a = []
for i in range(20):
    s = [x[i], y[i]]
    a.append(s)
a = np.array([a])
print(a)
print(a.shape)
print(type(a))


