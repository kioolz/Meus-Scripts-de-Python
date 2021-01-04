# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:24:51 2019

@author: Caio


"""

import matplotlib as plt

from matplotlib import bar


Filmes = ["Filme 1", "Filme2", "Filme3","Filme4", "Filme5"]
num_oscars = [5,11,3,8,10]

#As barras possuem o tamahno padrão de 0.8, então adicionaremos 0.1
#às coordenadas à esquerda para que cada barra seja centralizada

xs = [i + 0.1 for i, _ in enumerate(Filmes)]

 #as barras do gráfico com as coordenadas x à esquerda [xs], alturas [num_oscars]
 

plt.bar(xs, num_oscars)
plt.ylabel("# de premiações")
plt.title("Meus filmes favoritos")

#nomeia o eixo X com nomes de filmes na barra central 
plt.xticks ([i + 0.5 for i, _ in enumerate (Filmes)], Filmes)
plt.show()