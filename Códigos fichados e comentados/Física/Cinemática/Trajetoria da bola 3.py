# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 01:10:13 2019

@author: Caio
"""


# Formatação de texto com variáveis.
v0 = float(input()) #Velocidade inicial
print(v0) # Escreve o valor da velocidade inicial
g = 9.81 # Valor da gravidade
t = float(input()) # Variável tempo
y = v0*t - v0*g*t**2

print( """
At t=%f s, a  ball with
initial velocity v0 =%.3E m/s
is located at the height %.2f m. 
""") % (t, v0, y)

