#---------------------Visualização de dados em Python------------------
import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 7, 1, 8]

x2 = [7, 8, 9, 10, 11]
y2 = [0, 10, 5, 4, 7]

titulo = ["Gráfico de Barras 2 - Vendas de Ovos"]
eixoX = "Eixo X"
eixoY = "Eixo Y"

#Título
plt.title(titulo)

#Legendas
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.bar(x1, y1, label = "30 ovos por apenas R$ 10")
plt.bar(x2, y2, label = "Morangão")
plt.legend()
plt.show()