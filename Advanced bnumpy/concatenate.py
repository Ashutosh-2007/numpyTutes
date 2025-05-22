# To concatenate two arrays
'''
np.concatenate((arr1, arr2), axis = 0)
axis = 0 vertical stacking
axis = 1 horizontal stacking

np.delete(array, index, axis) function




'''

import numpy as np

arr = np.array([10,20,30,40,50,60])
# arr_2 = np.array([70,80,90,10,20,30])
# conc_arr = np.concatenate((arr,arr_2))
# print(conc_arr)

# for removing elements from array 

# new_arr = np.delete(arr, 2)
# print(new_arr)

# stacking 
'''
In NumPy, stacking refers to joining multiple arrays along a new axis. Unlike concatenate(), which merges arrays along an existing axis, stacking adds a new dimension in the process.

np.vstack() - stacks vertically (row-wise)

np.hstack() - stacks horizontally (column-wise)

'''

# print(np.vstack((arr,arr_2)))
# print(np.hstack((arr,arr_2)))


# splitting
arr_2d = arr.reshape(2,3)
spl_arr = np.vsplit(arr_2d,2)
for i in spl_arr:
    print(i)

# arr = np.array([1, 2, 3, 4, 5, 6])
# arr_2d = arr.reshape(2, 3)  # Now it's 2D: 2 rows, 3 columns

# splits = np.vsplit(arr_2d, 2)


# print(splits)