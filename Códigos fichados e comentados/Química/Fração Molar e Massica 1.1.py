# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:44:54 2019

@author: Caio
"""


class FraçãoMolareMassica():
    
    def FraçãoMolar():
    
        mols=int(input("Insira a quantidade mols da amostra", "\n"))
        print("Este foi o número de mols da amostra:", mols)
        
        totalmols=int(input("Insira a quantidade total de mols", "\n"))
        print("Este foi o número total de mols", totalmols)
        
        fraçaomolar=mols/totalmols
        print("Esta é a fração molar", fraçaomolar)
        
    FraçãoMolar()
    
    
    def FraçãoMassica():
        
        massa=float(input())
        print(massa)
        
        massatotal=float(input())
        print(massatotal)
        
        fraçaomassica=massa/massatotal
        print(fraçaomassica)
        
    FraçãoMassica()
    
    