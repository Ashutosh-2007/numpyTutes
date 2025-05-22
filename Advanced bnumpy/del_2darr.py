import numpy as np


arr_2d = np.array([[1,2,3],[4,5,6]])
new_arr = np.delete(arr_2d, 1,axis = 0)
print(new_arr)

''' if we pass axis then it will delete the whole 1 row but if we don't then it will just delete the elemnt at position 1'''