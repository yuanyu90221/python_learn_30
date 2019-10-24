import numpy as np

array_a = np.array([[[1,1,1,1],[2,2,2,2],[3,3,3,3]]])
array_b = np.array([0,1,2,3])
array_c = np.array([[1],[2],[3]])
array_d = np.array([[0,1,2,3],[0,1,2,3],[0,1,2,3]])
print(array_a + array_b)
print(array_a + array_d)
print(array_a + array_c)