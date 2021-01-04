# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:32:42 2019

@author: Caio



"""





#Definindo as variaveis associadas as moleculas

class Densidade:
    
    #Volume Específico
    
    def VolumeEspecifico():
        Volume=float(input())
        print(Volume)
        Massa=float(input())
        print(Massa)
        
        Ve=Volume/Massa
        print(Ve)
    VolumeEspecifico()
    
    #Densidade
    
    def Densidade():
        Volume=float(input())
        print(Volume)
        Massa=float(input())
        print(Massa)
        
        Densidade=Massa/Volume
        print ("Esta é a densidade", Densidade)
        
    Densidade()
    
    
    
    
        
        