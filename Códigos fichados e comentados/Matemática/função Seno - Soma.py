# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 13:06:08 2019

@author: Caio
"""

#Implementando a função Seno a partir da sua soma

x = 1.2 # Valor de controle para a variável X
N = 25 #Contador
k = 1 #Fatorial associado a vari[ável Sen   ]
s = x
sinal = #Sinal da função Seno

import math #Importando o módulo matemática

while k < N: #Enquanto o fatorial for menor que N
    sign = -sign #Sinal da função inverte em cada etapa da soma
    k = k + 2
    term = sign*x**k/math.factorial(k)
    s = s + term
    
print 'sin(%g) = %g (Aproximação com este %d termos)' % (x,s, N)


    