import matplotlib.pyplot as plt
import numpy as np


x = np.array([1, 4 , 5 , 6 , 7])
y = np.array([2, 6, 3  , 6 , 3])

# Lista de colores para cada segmento
colors = ['purple', 'red', 'blue', 'green', 'orange']

# Graficar cada segmento con un color diferente
for i in range(len(x) - 1):
    plt.plot(x[i:i+2], y[i:i+2], marker='o', color=colors[i], linestyle='-.')

plt.plot(x , y , marker='o' , color = 'purple' , linestyle = "-.")

plt.grid(True)
plt.show()