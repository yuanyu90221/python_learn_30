import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 10)
y_1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y_2 = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

plt.hist2d(x, y_2)
plt.show()