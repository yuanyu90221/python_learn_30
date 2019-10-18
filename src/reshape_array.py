import numpy as np

array_a = np.array([[1,2,3],[4,5,6]])

print(array_a.shape)
print(array_a.size)

array_b = array_a.T

#print(array_b)
print(array_b[0])
print(array_b[:,1])
print(array_b[0,0])