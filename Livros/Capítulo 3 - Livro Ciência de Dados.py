# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 22:01:35 2019

@author: Caio
"""





from matplotlib import pyplot as plt
import collections


years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]

#Cria um Gráfico de Linha, Anos no eixo X, GDP no eixo Y

plt.plot (years, gdp, color='green', marker='o', linestyle='solid')

#adiciona um Título

plt.title("GDP Norminal")

#Adiciona um selo no eixo Y
plt.ylabel ("Bilhões de $")
plt.show()


# Gráfico de Barras --- Este já é outro código, só estou anexando tudo no mesmo arquivo para não perder, se quiser testar esse trecho de código, então coloque em outro script


movies = ["Filme1", "Filme2", "Filme3", "Filme4", "Filme5"]
num_oscar = [5, 3, 11, 9, 12]

# Barras possuem o tamanho de padrão 0.8, então adicionarei 0.2 às # Coordenadas à esquerda para que cada barra seja centralizada

xs = [i + 0.1 for i, _ in enumerate (movies)]

plt.bar(xs,num_oscar)

plt.ylabel("#De premiações")
plt.title("meus filmes favoritos")

#Nomeia o Eixo X com nomes de Filmes na barra central

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()


# O próximo exemplo é de um Histograma 

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)


plt.bar([x - 4 for x in histogram.keys()], 
         histogram.values(), 
         8)

plt.axis([-5, 105, 0 , 5])
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decil")
plt.ylabel("# de Alunos")
plt.title("Distribuição das notas do Teste 1")
plt.show()


