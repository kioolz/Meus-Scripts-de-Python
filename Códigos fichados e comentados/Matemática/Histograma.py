# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 16:10:37 2019

@author: Caio
"""


# Contagem de amigos em um histograma - Usando Counter e plt.bar()

num_friends = [100,49,41,40,25]

friend_counts = Counter(num_friends)
xs = range(101)  #O valor maior é 100

ys = [friend_counts[x] for x in xs] #A altura é somente # de amigos

plt.bar (xs, ys)
plt.axis ([0, 101, 0, 25])

plt.title ("Histograma da contagem de amigos")

plt.xlabel ("# de amigos")
plt.ylabel ("# de pessoas")
plt.show()


#Número de pontos nos dados
num_points = len[num_friends]



#Maiores e menores valores
largest_value = max(num_friends)
smallest_value = min(num_friends)


#Casos especiais de valores em posições específicas

sorted_values = sorted(num_friends) #Organiza em ordem crescente

smallest_value = sorted_values[0] #Pega o primeiro valor da lista depois de ordená-la em ordem crescente

second_smallest_value = sorted_values[1] # Segundo valor da lista, técnica de indexação de listas e exibição de elemento

second_largest_value = sorted_values [-2] #Usa o negativo da lista para buscar na lista ao contrário depois de ordená-la



#Define a função média

def media(x):
    return sum(x)/len(x)
media(num_friends)



#Função Mediana

def mediana(v):
    
    """Encontra o valor mais ao meio de v"""
    
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n//2
    
    if n % 2 ==1:
        #Se for impar, retorna o valor do meio
        return sorted_v[midpoint]
    
    else:
        #Se for par, retorna a media dos valores do meio
        
        lo = midpoint - 1
        hi = midpoint
    
    return (sorted_v[lo] + sorted_v[hi]) /2 

mediana(num_friends)    


