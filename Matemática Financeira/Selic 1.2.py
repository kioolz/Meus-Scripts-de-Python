# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 01:33:53 2019

@author: Caio
"""

#Taxa Selic
taxaselic=(5.5/36500) #  ( 5.5/100 ) 365 para transformar de ano para dia


#Tabela regressiva do IR
IR1=22.5/100
IR2=20/100
IR3=17.5/100
IR4=15/100
IOF=1

Valoraplicado=float(input('Insira o valor aplicado'))                    
tempoaplicadoemdias=int(input('Insira o número de dias que o valor ficou aplicado'))




#Estrutura condicional para estabelecer o cálculo do IR 
#para os dias que o valor ficou rendendo na SELIC
if ((tempoaplicadoemdias)<180):
    valorfinal = Valoraplicado + (Valoraplicado * tempoaplicadoemdias * IR1 * taxaselic)
    print(valorfinal)
if ((tempoaplicadoemdias)>180 and (tempoaplicadoemdias)<360):
    valorfinal = Valoraplicado + (Valoraplicado * tempoaplicadoemdias * IR2 * taxaselic)
    print(valorfinal)
if ((tempoaplicadoemdias)>180 and (tempoaplicadoemdias)<720):
    valorfinal = Valoraplicado + (Valoraplicado * tempoaplicadoemdias * IR3 * taxaselic)
    print(valorfinal)
if ((tempoaplicadoemdias)>(720)):
    valorfinal = Valoraplicado + (Valoraplicado * tempoaplicadoemdias * IR4 * taxaselic)
    print(valorfinal)





          



