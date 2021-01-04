# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:52:13 2019

@author: Caio
"""

X = 1
Y = 1

print ('{:>4}' .format (' '), end= ' ')
for X in range (1, 11):
    print ('{:>4}'. format(X), end= ' ')
    
print ()

for X in range (1,11):
    print ('{:>4}'. format(X), end = ' ')
    while Y <=10:
        print('{:>4}' . format (X * Y), end= ' ')
        Y+=1
    print ()
    Y=1
    
#------------------------------------------------------------
    # Treino de Matriz
    
X = 1 
for X in range  (1, 15):
    print (X)
    print ('{:>4}' .format (' '), end= ' ')