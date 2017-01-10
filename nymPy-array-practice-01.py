import numpy as np

# Manual construction of arrays


# one dimension array
a = np.array([0,1,2,3])
print(a)

print ('dimension', a.ndim)

print('shape', a.shape)

print('length', len(a))

# two dimension array

b = np.array([[0,1,2], [3,4,5]])
print(b)

print('dimension', b.ndim)

print('shape', b.shape)

print('length', len(b))

# Functions for creating arrays
# Evenly spaced
a = np.arange(10)
print('0,1,2,.....n-1', a)

b = np.arange(1, 9, 2)
print('start 1, end 9(exclusive), step 2', b)

# number of points
a = np.linspace(0, 1, 6)
print('start, end, num-points', a)

a = np.linspace(0, 1, 5, endpoint=True)
print('start, end, num-points, endpoint = false', a)




