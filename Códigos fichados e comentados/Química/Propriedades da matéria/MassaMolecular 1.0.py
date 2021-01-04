# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:24:02 2019

@author: Caio
"""

class MassaMolecular():

    
    #Definindo as variaveis associadas as moleculas
    print ("Insira a massa da substância")
    Massa = float(input())
    print ("Insira a quantidade de mols da substância")
    Mol = float(input())
    
    def MassaMolecular(Massa,Mol):
        MassaMolecular=Massa/Mol
        print ("Esta é a massa molecular da substância", MassaMolecular)
    MassaMolecular(Massa,Mol)




