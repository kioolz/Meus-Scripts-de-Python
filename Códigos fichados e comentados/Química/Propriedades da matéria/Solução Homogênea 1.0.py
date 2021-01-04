# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:25:18 2019

@author: Caio
"""

#Código da mistura homogênea    
    
Massaparcial=float
Massatotal=float
Volumeparcial=float
Volumetotal=float
Volume=float
m=float
v=float
DensidadedaSoluçao=float
v = []
m = []
    
def SoluçãoHomog ():
    
    Massaparcial = float(input("Digite as massas [0 para terminar]"))
    Massatotal = 0
    
    while Massaparcial!=0:
        Massatotal = Massaparcial + Massatotal
        Massaparcial = float(input(("Digite o valor da proxima massa ou aperte 0 para terminar")))
        m.append(Massaparcial)
    Volumeparcial = float(input("Digite os volumes [0 para terminar]"))
    Volumetotal = 0
    while Volumeparcial !=0:
        Volumetotal = Volumeparcial + Volumetotal
        Volumeparcial = float(input("Digite o volume parcial da próxima substancia ou aperte 0 para terminar"))
        v.append(Volumeparcial)
    
    if len(m) == len(v):
        DensidadedaSoluçao=Massatotal/Volumetotal
        print ("A massa total é ", Massatotal)
        print ("O volume total é", Volumetotal) 
        print ("A densidade da solução é ", DensidadedaSoluçao)
    else:
        print("Você não inseriu a mesma quantidade de massas e volumes, erro")
   
   
#-----se colocar 0 nos 2 é pra parar a soma.----------
SoluçãoHomog()