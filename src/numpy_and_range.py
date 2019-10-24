import numpy as np

array_a = np.arange(0,100,5)
print(array_a)
print(array_a.size)

array_a_reshape = array_a.reshape(4,5)
print(array_a_reshape)

# neg indexing
print(array_a_reshape[:,-1])

# boolean indexing
array_a_above_50 = array_a_reshape[array_a_reshape >= 50]
print(array_a_above_50)

# python slice
print(array_a_above_50[0:len(array_a_above_50):2])

# slice of a row
print(array_a_reshape[:,0:5:2])

print(np.where(array_a_reshape>50, array_a_reshape*2, -1))