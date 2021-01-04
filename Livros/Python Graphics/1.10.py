# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:57:43 2019

@author: Caio
"""

#Customizando linhas de grade

import numpy as np
import matplotlib.pyplot as plt

x1 = -5
x2 = 15
y1 = -15
y2 = 5

plt.axis([x1,x2,y1,y2])

plt.axis('on')

dx=.5 # Espaçamento pro X
dy=.5  # Espaçamento pro Y

for x in np.arange(x1,x2,dx): #Localização dos X
    for y in np.arange(y1,y2,dy): #Localização dos Y
        plt.scatter(x,y,s=1,color='blue')  # Plote um ponto azul no ponto X , y 




plt.xlabel('este é o eixo X') # Descrição das variáveis nos eixos
plt.ylabel('este é o eixo Y')          # Descrição das variáveis nos eixos
plt.title('Este é o título') # E assim aidiconamos um título ao gráfico
plt.show()




