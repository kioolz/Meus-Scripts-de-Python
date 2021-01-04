# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:52:13 2019

@author: Caio
"""

X = 1 # Definindo as variáveis X e Y para construir a matriz numérica
Y = 1

print ('{:>4}' .format (' '), end= ' ') # ????
for X in range (1, 11): # Definindo a condição for para o range da matriz
    print ('{:>4}'. format(X), end= ' ')
    X+=1
print ()

for X in range (1,10):
    print ('{:>4}'. format(X), end = ' ')
    while Y <=10:
        print('{:>4}' . format (X * Y), end= ' ')
        Y+=1
    print ()
    Y=1
    
    