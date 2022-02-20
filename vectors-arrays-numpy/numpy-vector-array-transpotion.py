import numpy as np

x = np.arange(3)
y = np.arange(4)
z = np.arange(3)

print('np.arange(3)', x)
print('x.T == x', x.T == x)

print('x.T == y', x.T == y)
print('x.T == z', x.T == z)

