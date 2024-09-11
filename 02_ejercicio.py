import matplotlib.pyplot as plt
import numpy as np


x = np.array([10, 20 , 30])
y = np.array([20, 40, 10])
m = np.array([10, 20 , 30])
n = np.array([40, 10, 30])


plt.plot(x , y , marker='o' , color = 'pink')
plt.plot(m, n, marker='s', color='green', label='Línea 2') 
plt.grid(True)
plt.show()