# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 18:53:52 2019

@author: Caio
"""


# Se eu aplicar uma quantidade fixa de dinheiro num intervalo fixo de tempo
#Rendendo a uma % fixa de juros , depois de um intervalo X de tempo
# A taxa de juros seria a taxa SELIC, menos os descontos do imposto de renda e do IOF. 
#Essas condições então tem de estar muito específicas


# O programa deve printar os resultados em formato de DataFrame no final do código


# 1.0 - Preciso colocar o datetime como uma forma de controlar a indexação do dataframe.

# Plote o gráfico associado ao montante
import pandas as pd
from pandas import DataFrame, Series
from datetime import datetime


#Contador para funcionar o while
j=0


#Listas vazias que serão preenchidas no while e servirão pro dataframe
AportesMensais=[]
IntervalosdeTempo=[]
RendimentosRelativos=[]
MontantesRelativos=[]


#Taxa de Juros
TaxadeJuros=(5.5/100)/12
TaxasdeJuros=[]

total=0
TotaisRelativos=[]


Intervalodetempo=int(input('Por quantos meses você vai deixar o dinheiro rendendo?' ))

while (Intervalodetempo!=j):
    
    Aporte=float(input('Insira o valor do aporte'))
    AportesMensais.append(Aporte)
    
    IntervalosdeTempo.append(j) #Indexa o intervalo de tempo na lista como variável
    TaxasdeJuros.append(TaxadeJuros) #Insere a taxa de juros relativa ao período
    
    
    
    RendimentoUnitario = Aporte * TaxadeJuros # Define o rendimento líquido do mês
    RendimentosRelativos.append(RendimentoUnitario) # Insere o rendimento líquido do mês na lista
    
    
    MontanteRelativo=RendimentoUnitario+Aporte #Operação para o rendimento do mês
    MontantesRelativos.append(MontanteRelativo) #Rendimentos líquidos de cada mês

    if (Aporte==0):
        
        total = (Aporte + (1 + TaxadeJuros)**(Intervalodetempo+j)) + total
        TotaisRelativos.append(total)
        j=j+1 #Aumenta o contador
        
    else:
        total = (Aporte * (1 + TaxadeJuros)**(Intervalodetempo+j)) + total
        TotaisRelativos.append(total)
        j=j+1

#Criando o DataFrame que vai armazenar todos os valores
df = pd.DataFrame({'Mês':IntervalosdeTempo,'Aportes':AportesMensais,
                   'JurosMensal':TaxasdeJuros,'Rendimento Líquido': RendimentosRelativos,'Totais': TotaisRelativos})
df



