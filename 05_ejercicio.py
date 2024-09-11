import matplotlib.pyplot as plt
import numpy as np

# Crear datos similares a los que se muestran en la imagen
x = np.linspace(0, 5, 20)  # 20 puntos entre 0 y 5
y1 = x ** 2  # y1 es x al cuadrado
y2 = x ** 3  # y1 es x al cubo
y3 = x ** 0.3

# Crear el gráfico

plt.plot(x, y1, 's', color='b', label='Cuadrados')  # Marcadores cuadrados
plt.plot(x, y2, '^', color='brown', label='Cubos')  # Marcadores
plt.plot(x, y3,  color='green', label='Lineas' , linestyle='--')  

plt.xlabel('X ')
plt.ylabel('Y')
plt.legend()


plt.show()
