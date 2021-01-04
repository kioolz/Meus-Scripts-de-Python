# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 22:04:18 2019

@author: Caio
"""

def main ():
    num=int(input("Digite um numero inteiro [0 para terminar]:"))
    soma = 0
    
    while num !=0:
        soma = soma + num
        num = int(input("Digite um inteiro [0 para terminar]: "))
        
    print ("A soma foi ", soma)    
#------------------
main()
        
        