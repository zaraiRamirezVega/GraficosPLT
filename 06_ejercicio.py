import matplotlib.pyplot as plt


fecha = ['2016/10/03' , '2016/10/04' ,'2016/10/05' ,  '2016/10/06 ' , '2016/10/07']
valores = [772.5 , 776.5 , 776.6 , 777.0  , 775.0]


plt.plot(fecha , valores , marker='o' , color = 'pink' , linestyle = "-")


#Añadir etiquetas
for i , valor in enumerate(valores):
    plt.text(i , valor  , f'{valor}' , ha = 'right' , va = 'bottom')

plt.grid(True)
plt.xlabel('Fecha')
plt.ylabel('Valores')
plt.show()