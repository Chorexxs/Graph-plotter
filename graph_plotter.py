# Programa para crear gráficas con la librería matplotlib

import matplotlib.pyplot as plt

# con los ejes x e y se hacen 2 listas que contienen las coordenadas

x1 = [2, 4, 5]
y1 = [2, 3, 6]

# plt.plot(x, y) para determinar la customización de las líneas

plt.plot(x1, y1, linestyle="dashed", label="Line 1")

x2 = [1, 2, 3, 4]
y2 = [1, 2, 3, 4]

plt.plot(x2, y2, marker="o", label="Line 2")

# plt.xlabel y ylabel son para marcar el eje de las x y de las y

plt.xlabel("X axis")
plt.ylabel("Y axis")

# plt.title("Nombre de la gráfica")

plt.title("Demo graph")

# plt.legend() muestra la leyenda de las líneas

plt.legend()

# plt.show() ejecuta la gráfica

plt.show()
