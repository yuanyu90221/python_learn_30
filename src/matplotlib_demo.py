import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 50)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='Exponential')
plt.plot(x, x/2, label='half linear')
plt.xlabel('X axios label')
plt.ylabel('Y axios label')
plt.title('This is the title of our graph')
plt.show()