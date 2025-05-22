import numpy as  np
import time as t

# python_List = [1,2,3,4,5]
# print(python_List)


py_array = np.array([1,2,3,4,5])
# print(py_array)

# one dimensional array

ar_1d = np.array([1,2,3,4,5])
# print(ar_1d)

# two dimensional array

ar_2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
# print(ar_2d)

# To calculate time taken to perfm operation by list and numpy array

# start = t.time()
# py_List = [i*2 for i in range(100000)]
# print("\n List operation time: ", t.time() - start)

# start = t.time()
# np_arr = np.arange(100000) * 2
# print("\n Numpy array operation time: ", t.time() - start)

# Matrix

matrix = np.array([
    [2,4,6],
    [8,10,12]
    ])
# print(matrix)

# matrix with default values

zero_arr = np.zeros((2,3))
ones_arr = np.ones((2,3))
filled_arr = np.full((3,3),1)
idn_mtrx = np.eye(3,3)

# print(zero_arr)
# print(ones_arr)
# print(filled_arr)
# print(idn_mtrx)


# Creating seq of nmber in numpy
# arange(start,stop,step) similar as range but just to create sequence

arr = np.arange(1,100,2)
print(arr)