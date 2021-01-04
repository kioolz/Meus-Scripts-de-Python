# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:22:07 2019

@author: Caio
"""


# A constante de Boltzmann (k) vale 1.380 * 10^-16 erg/grau, de modo que cada molécula tem energia cinética 3kT/2


class ConstantedeBoltzmann:
    
    def EnergiaCineticaMolecula():
        
        k = 1.380*(10**-16)
        print ("A constante de Boltzmann possui o valor igual a:", k, "erg/grau")
        T=float(input()) #Temperatura absoluta
        print(T)
        E = (3/2) * k * T 
        print("A temperatura escolhida", T, "Produz a energia", E)
        
    EnergiaCineticaMolecula()
    

        
        