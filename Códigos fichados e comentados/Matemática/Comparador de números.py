# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:41:30 2019

@author: Caio
"""
# Este código é um comparador entre números inseridos pelo usuário.

print ("Insira dois valores para serem comparados:")



Valor1= float(input("Escreva um número:"))
Valor2= float(input("Escreva outro número:"))

Númerosarmazenados=[]

Númerosarmazenados.append(Valor1,Valor2)


print ("Os números que você inseriu foram esses?","\n", Valor1, "\n", Valor2)

sim = str
não = str

while (str(input())!="não") or (str(input())=="sim"):
    
    if str(input(sim)):
        if (Valor1 > Valor2):
            print ("O primeiro valor é maior que o segundo")
            print (Númerosarmazenados)
        if (Valor2 > Valor1):
            print ("O segundo valor é maior que o primeiro")
            print (Númerosarmazenados)
        if (Valor2 == Valor1):
            print ("Os números são iguais")
            print (Númerosarmazenados)
        
    if str(input(não)):
        print ("Então insira os números corretos")
        break
    

    


        



    
    