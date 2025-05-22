''' 

Flattening means converting multi dim arr into 1 d arr
ravel also does the same thing but it returns the view anf flatten returns the copy
view can modify the original array
but copy will not!

'''

import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.flatten())
print(arr_2d.ravel())
