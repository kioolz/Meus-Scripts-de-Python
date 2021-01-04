# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:43:24 2019

@author: Caio
"""


#Criei listas vazias para armazenar as variáveis de cada etapa

variaveis=[] #Aqui eu defino a lista de variáveis inseridas

totalparcial=[] #Aqui eu defino o total acumulado pelas variáveis em cada etapa da soma
#Basicamente é a sequência das somas parciais


mediasparciais=[]  # Aqui é o valor da média entre cada etapa.

def Media(): #Defino a função média
    
    total=0 #Estabeleço a variável Total como sendo 0 
    
    while total!=str: #Enquanto o total não for uma letra (por razões óbvias)
        print ("Insira as variáveis para o cálculo")
        Valor=float(input()) #Um Valor real será inserido pelo usuário 
        print ("Esta é a lista de variáveis definidas pelo usuário") #Exibe uma mensagem que mostra a lista de variáveis
        variaveis.append(Valor) #Insere as variáveis Valor dentro da lista de Variáveis
        #No caso, armazena a variável em cada etapa
        print(variaveis)
        
        # Acrescenta o valor Total.
        total=Valor+total
        
        #Insere as variáveis Total em uma lista contendo todas elas.
        totalparcial.append(total)
        print("Esta é a lista do valor total em cada etapa")
        print(totalparcial)
        
        #Aqui se faz o cálculo da média
        Media=total/len(totalparcial)
        #Aqui armazena os valores da média em cada etapa 
        print ("Esta é a lista das médias em cada etapa inserida pelo usuário")
        mediasparciais.append(Media)
        print(mediasparciais)
        
        print ("Esta é a média ao final de todas as etapas")
        print(Media)
        
    
Media()


