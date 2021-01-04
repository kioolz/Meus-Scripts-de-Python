# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 12:17:15 2019

@author: Caio
"""

#Algoritmo simples para o método de Newton-Raphson.

def Newtonraphson(n, ni = 500):
    a = float(n) # n é o valor principal
    for i in range (ni): #ni é o contador de interações
        n = 0.5 * (n + a / n)
    return n

print (Newtonraphson(10))
print (Newtonraphson(11))
print (Newtonraphson(12))
print (Newtonraphson(13))
print (Newtonraphson(14))
print (Newtonraphson(15))
print (Newtonraphson(16))
print (Newtonraphson(17))
print (Newtonraphson(18))
print (Newtonraphson(19))
print (Newtonraphson(20))


