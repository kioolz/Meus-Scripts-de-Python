# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 00:55:00 2019
@author: Caio
"""
# Código pertencente aos problemas que envolvem a termologia

Celsius=str
Fahrenheit=str

class Termologia():
    
    def ConverterCpraF():
        
        print ("Digite a escala de temperatura que deseja converter")
              

        print ("Digite Celsius ou Fahrenheit para escolher")
        
        if str(input(Celsius)):
            print ("Insira o valor da temperatura em celius")
            C=float(input())
            F = (C * 9/5) + 32
            print("Correspondem à ", F, "Fahrenheit")
            
        if str(input(Fahrenheit)):
            print ("Insira o valor da temperatura em Fahrenheit")
            F = float(input())
            C = (F - 32) * 5/9
            print ("Correspondem à", C, "Celsius")
            
    ConverterCpraF()
    
    
    def ConverterCpraF2():
        
        escala = int(input('Digite [1] para Celsius , [2] para Fahrenheit: '))
    
        
        if escala == 1:
            C=float(input("Insira o valor da temperatura em celius"))
            F = (C * 9/5)   + 32
            print('{} Celsius correspondem à {} Fahrenheit'.format(C,F))
            
            
        elif escala == 2:
            F = float(input('Insira o valor da temperatura em Fahrenheit: '))
            C = (F - 32) * 5/9
            print ('{} Fahrenheit correspondem à {} Celsius'.format(F,C))
            
    ConverterCpraF2()
           
    
    