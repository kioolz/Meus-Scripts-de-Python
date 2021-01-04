# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 01:34:25 2019

@author: Caio
"""



from math import pi,tan, cos

# Aceleração da gravidade.
print ("Insira o valor da gravidade do local")
g = float(input()) #(m/s**2)

print ("Insira o valor da velocidade inicial")
v0 = 15

print ("Insira o valor do ângulo")
theta = 60.0

print ("Insira o valor da posição inicial")
x = 0.5

print ("Insira o valor da altura inicial")

y0 = 1.0

print ("""\

v0 = %.1f km/h
theta = %d degrees
y0 = %.1f m
x = %1f m\
""") % v0,theta,y0, x


# Converter v0 to m/s e theta para radianos
v0 = v0/3.6
theta = theta*pi/180.0

y = [(x*tan(theta)) - (1.0/((2.0*v0**2.0)*g*x**2.0)/((cos(theta))**2.0)) + y0]


print ('y= %.1f m') %y
