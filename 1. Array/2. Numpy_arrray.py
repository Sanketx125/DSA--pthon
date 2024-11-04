

import numpy as np
'''
    * numpy arrays default value is fload.
'''


print('\n----------------------------------------------\n')
# numpy array:
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

print('\n----------------------------------------------\n')

# creating array with all zeros:
zero = np.zeros((2,3))   # 2D array with 2-rows & 3-columns
print('creating array with all zeros:\n',zero)

print('\n----------------------------------------------\n')

# creating array with all one:
one = np.ones(((2, 3)))  # 2D array with 2-rows & 3-columns
print('creating array with all one:\n',one)

print('\n----------------------------------------------\n')

# creating array with constant values:
const = np.full((2, 3), 5)
print('Constant value array:\n',const)

print('\n----------------------------------------------\n')

# Creating array with identity matrix
idn = np.eye(2)
print("identity Matrix array:\n",idn)

print('\n----------------------------------------------\n')

# creating array of random values:

rand1 = np.random.random((2, 2))
print("array of random values:\n", rand1)

print('\n----------------------------------------------\n')