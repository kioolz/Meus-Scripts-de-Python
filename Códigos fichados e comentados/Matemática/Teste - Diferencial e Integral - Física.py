# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 23:42:54 2019

@author: Caio
"""

# O seguinte exemplo demonstra como diferenciar a formula referente ao lançamento obliquo
# Vo * t - 1/2 g*t^2 

from sympy import (
        symbols, #Define os simbolos matemáticos
        diff, #Diferenciar expressões
        integrate, #Integrar expressões
        Rational, #Define numeros racionais
        )

t, v0, g = symbols('t v0 g')
y = v0*t - Rational(1,2)*g*t**2
dydt= diff(y, t)
dydt-g*t + v0
print ('acceleration:', diff(y, t , t)) #Segunda derivada
acceleration: -g
y2 = integrate(dydt, t)
print(y2)