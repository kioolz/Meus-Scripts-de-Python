# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:21:05 2019

@author: Caio
"""


#Plotando um gráfico simples


# Módulos necessários

import numpy as np
import matplotlib.pyplot as plt



#Limites dos eixos coordenados
x1 = -10
x2 = 150

y1 = 90
y2 = 10

# Comando que inicia os eixos limitados por variáveis definidas pelo usuário
plt.axis([x1,x2,y1,y2])


#Liga o gráfico
plt.axis('on')


 # Adiciona uma grade ao gráfico e uma cor 
plt.grid(True, color='green')
plt.title('Título do gráfico')

#Minimizando os intervalos da grade de valores do gráfico

#Estabelecendo os valores máximos e minimos para X e o intervalo de separação da grade
xmin=x1
xmax=x2
dx=10 # Intervalo estabelecido para o Tick

#Estabelecendo os valores máximos e minimos para Y e o intervalo de separação da grade
ymin=y1
ymax=y2
dy=-5 #Intervalo estabelecido para o tick 


#Comando Ticks para separar os intervalos da grade em porções menores.
plt.xticks(np.arange(xmin,xmax,dx))
plt.yticks(np.arange(ymin,ymax,dy))


#Exibe o gráfico no console
plt.show()



