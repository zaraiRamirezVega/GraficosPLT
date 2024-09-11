import matplotlib.pyplot as plt
import numpy as np


x = np.array([10, 20 , 30])
y = np.array([20, 40, 10])



plt.plot(x , y , marker='o' , color = 'pink')

plt.grid(True)
plt.show()