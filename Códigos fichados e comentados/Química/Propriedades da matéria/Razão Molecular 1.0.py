# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:25:01 2019

@author: Caio
"""

#Razão molecular
 #Se dois elementos A e B formarem mais de um composto, 
#as massas de A que se combinam com a mesma massa de B, nos diferentes compostos, devem ter
# como razões, números inteiros.


class RazãoMolecular:
    

    def rm():
    
        Massas1=[]
        Massas2=[]
        Razoes=[]
        while len(Massas1)==len(Massas2):
            
            print ("Insira a massa do primeiro elemento")
            m1=float(input())
            Massas1.append(m1)
            print ("Insira a massa do segundo elemento")
            m2=float(input())
            Massas2.append(m2)
            r=m1/m2
            Razoes.append(r)
            print("O valor da massa do numerador é:",m1,"gramas")
            print("O valor da massa do denominador é:",m2,"gramas")
            print ("O valor da razão molecular as duas últimas massas foi ", r, "gramas")
            print("A lista de massas inseridas no numerador", Massas1)
            print("A lista de massas inseridas no denominador", Massas2)
            print("A lista de razoes calculadas é", Razoes)
    
   

    rm()
    
    