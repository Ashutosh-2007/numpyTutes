'''

np.insert(arr, index, value, axis) 
arr = og array
index = index where we wan to insert
value we need to change 
axis to change in row axis = 0 and to change in column we will put axis  = 1

'''

import numpy as np

# inserting a value 

arr = np.array([1,2,3])
ins_arr = np.insert(arr,2, 54,axis = None)
# print(ins_arr)

# Working with 2d array

arr_2d = np.array([[1,2],[4,5]])

# print(arr_2d.ndim)
ins_arr_2d = np.insert(arr_2d, 2,[7,6],axis = 1)
# print(ins_arr_2d)

# appending in an array --> it returns new array and doesn't changes original one

new_arr = np.append(arr,[40,50,60])
# print(new_arr)



