# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:27:13 2019

@author: Caio
"""

# Cálculo Simples do rendimento do tesouro SELIC




#Importando a biblioteca Pandas para construir a tabela de dados
import pandas as pd


#Criando o DataFrame com as colunas. 
df = pd.DataFrame(columns=['Aporte','Tempo'])


# Criando a função Investimento
def investimento():
    #Esta é a taxa SELIC - Setembro/2019
    TaxaSelic=0.6
    
    #Contadores que servem pro While funcionar
    i = 1
    j = 1
    
    
    #Estrutura condicional para usar o While.
    while (i < 6) and (j < 6):
        
        
        
        #Variável Aporte Mensal
        aporte = float(input('Entre com o valor do investimento: '))
        
        #Variável Tempo de Aplicação
        tempo = int(input('Entre com o número de dias para o investimento: '))
        
        #Dicionário com os valores da tabela
        user_data = {'aporte': aporte, 'tempo': tempo}
        
        #Somatório dos contadores para fechar o While
        i=i+1
        j=j+1
    
    
    return user_data

df = df.append(investimento(), ignore_index=True)



#Essa é a variável que insere o valor inicial investido

print ("Insira o valor do investimento inicial")
Investimentoinicial=input(float())

print ("Insira o tempo que este valor ficará parado rendendo")
tempo = input(int())

IOF = 0.65
IR = 22.5/100

Rendimento = Investimentoinicial 

print (Rendimento)  