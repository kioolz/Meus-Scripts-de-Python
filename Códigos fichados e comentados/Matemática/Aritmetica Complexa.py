# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 23:34:18 2019

@author: Caio
"""



# Exemplo de Aritmética complexa 

u = 2.5 + 3j  #Criando um numero complexo 
 
v = 2
 
w = u + v # Operação soma

print(w)


a = -2

b = 0.5

s = a + b*1j

s = complex(a,b)

s

s* w #Complex * Complex

s/w #Complex/Complex


#Partes do numero complexo

#Parte real
s.real
#Parte imaginaria
s.imag
#Conjugado
s.conjugate()



# Funções complexas com Python