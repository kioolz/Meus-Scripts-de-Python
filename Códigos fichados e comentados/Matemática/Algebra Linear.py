# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:39:00 2019

@author: Caio
"""
#Script usado para treinar Algebra Linear 

# A Algebra Linear é o ramo da matemática que lida com espaços vetoriais


# Definindo a Adição entre as componentes  
def vector_add(v,w):
    "Soma dos elementos correspondentes"
    return[v_i + w_i for v_i, w_i in zip(v,w)]
    
    
# Definindo a Subtração entre dois vetores
def vector_sub(v,w):
    "Subtrai os elementos correspondentes"
    return [v_i - w_i for v_i, w_i in zip(v,w)]


# Definindo Um novo vetor com a soma dos vetores 
    def vector_sum(vectors):
        "Soma todos os elementos correspondentes"
        result = vectors[0]
        for vector in vectors[1:]:
            result = vector_add(result,vector)
        return result
    
    
# Definindo a multiplicação por um escalar 
def scalar_multiply(c, v):
    return [ c* v_i for v_i in v]
        
        
        
# Definindo dois vetores simples
    
            
x = [1,2,3,4,5]
y = [5,4,3,2,1]

import numpy as np

# Redefinindo o Vetor como uma matriz, a matriz Z

z = np.array([1,2,3,4,5])

print (z)
print (type(z)) # Type (numpy.ndarray)
print (type(x)) # Type list
print (type(y)) # Type list

# É mais vantajoso definir todas as matrizes numéricas pela biblioteca numpy


#Operações básicas com a matriz
print (z + z)
print ( z - z)
print ( z * z)

# Definindo uma matriz  através da biblioteca Numpy

M = np.array ([[1, 2, 3], [3, 2, 1], [ 5, 7, 18]])




# Exibindo a matriz M na tela
import numpy as np
M = np.array ([[1, 2, 3], [3, 2, 1], [ 5, 7, 18]])
print (M)

#Exibindo as dimensões da matriz M na tela.
import numpy as np
M = np.array ([[1, 2, 3], [3, 2, 1], [ 5, 7, 18]])
print (M.shape)

# Transposta da Matriz
import numpy as np
M = np.array ([[1, 2, 3], [3, 2, 1], [ 5, 7, 18]])
print ('Matriz transposta:\n', M.transpose(), '\n')

# Determinante da matriz
import numpy as np
M = np.array ([[1, 2, 3], [3, 2, 1], [ 5, 7, 18]])
print ('Determinante da matriz:', np.linalg.det(M), '\n')

#Inversa da matriz
import numpy as np
M = np.array ([[1, 2, 3], [3, 2, 1], [ 5, 7, 18]])
m_inv = np.linalg.inv(M)
print ('Matriz inversa: \n', m_inv, '\n')

#Matriz identidade (Resultado da matriz * Matriz inversa)
import numpy as np
M = np.array ([[1, 2, 3], [3, 2, 1], [ 5, 7, 18]])
iden_m = np.dot(M, m_inv)
iden_m = np.round(np.abs(iden_m), 0)
print ('Produto da matriz e sua inversa:\n', iden_m)

#Decomposição da Matriz em AutoValores e Auto Vetores

import numpy as np
M = np.array([[1,2,3],[4,5,4],[2,6,1]])

auto_val, auto_vet = np.linalg.eig(M)

print ('Auto Valores:', auto_val, '\n')
print ('Auto Vetores:\n', auto_vet)

#Decomposição de Valor Singular - Decomposição SVD 
import numpy as np
M = np.array([[1, 2, 3], [4, 7, 9], [ 5, 4, 2]])

U, S, VT = np.linalg.svd(M)

print('Conseguindo uma saida para o SVD:-\n')
print('U:\n', U, '\n')
print('S:\n', S, '\n')
print('VT:\n', VT, '\n')












