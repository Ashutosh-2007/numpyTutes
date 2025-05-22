import numpy as np

aray = np.full((3,2),5)
# print(aray)
# print(aray.shape)
# print(aray.size)

multi_array = np.array([[1,2,3],[2,4,6],[6,5,4],
                [3,6,9],[4,18,12],[9,8,6],
                [3,6,9],[4,18,12],[9,8,6]])
mlti_array = np.array([[[1,2],[2,4],[4,5],[5,6]]])
# print(multi_array.ndim)
# print(mlti_array.ndim)


arr = np.array([10,20,30,40,50,60])

# print(arr.dtype)
# print(arr.astype(str))


# print(arr * 5)
# print(arr + 5)
# print(arr - 5)
# print((arr / 5).astype(int))
# print(arr ** 5)
# print(arr % 5)

# Let's see at some more mathematical operations

# print(np.sum(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.std(arr))
# print(np.var(arr))
# print(np.mean(arr))