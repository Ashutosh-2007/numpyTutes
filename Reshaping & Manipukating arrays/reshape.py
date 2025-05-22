''' 
changing the shape of array without changing or modifying actual data

Reshaping Never creates a copy

'''

import numpy as np

# arr = np.array([1,2,3,4,5,6])

# way 1

# Reshaped_arr = arr.reshape(4,2)
# print(Reshaped_arr)
# print(Reshaped_arr.ndim)

# way 2
# print(arr.reshape(3,3))

arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3)
print(arr3.ndim)

# arr_3d = arr.reshape(1, 2, 3)
# print(arr_3d.shape)