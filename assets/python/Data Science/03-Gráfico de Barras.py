#Visualização de dados em Python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 8]
titulo = ["Gráfico de Barras"]
eixoX = "Eixo X"
eixoY = "Eixo Y"

#Título
plt.title(titulo)

#Legendas
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.bar(x, y)
plt.show()