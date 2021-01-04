v# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 21:19:40 2019

@author: Caio
"""
#Importando a biblioteca que indexa os gráficos no compilador
from matplotlib import pyplot as plt
#---------------------------------------



#Definindo as variáveis dos eixos X e Y

#---------------------------------------------


X = [1.0,2.0,3.0,4.0]
T = [2.0,4.0,6.0,8.0]

#Definindo a equação da velocidade média 


 # Agora para atualizar este código.
 # Eu quero trocar a lista de valores das variáveis por um Input onde eu possa inserir os valores
 # E eu quero fazer isso quantas vezes eu quiser, porém o gráfico do MU compreende todos os valores dentre os reais.

#Definindo as propriedades do gráfico
plt.plot (X, T, color='blue', marker = 'o', linestyle = 'solid')

#Adiciona um Títutlo
plt.title = ("Movimento Uniforme")

plt.ylabel = ("Posição")
plt.xlabel = ("Tempo")

plt.show()


    
    