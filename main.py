# This is my learning journey to understand Numpy

import numpy as np
# create one dimensional numpy array
var1 = np.array([2,4,5])
print(var1)

# create two dimensional numpy array
var2 = np.array([(2,4,6), (1,3,5)])
print(var2)

# make another array
var3 = np.array([(2,4,6),(4,2,6,)])
# add arrays
print(var2+var3)

# basic calculations
# create new arrays
arr1 = np.array([2,4,6])
print(arr1)
# item size
print(arr1.itemsize)
# data type of the element inside the array
print(arr1.dtype)
# how many dimension inside the array
print(arr1.ndim)

arr2 = np.array([(2,4,6), (2,4,6),(1,3,5)])
print(arr2)
print(var2.size)

# shape of array, how many rows and cols
print(arr2.shape)

# reshape array var2
var2 = var2.reshape(3,2)
print(var2)