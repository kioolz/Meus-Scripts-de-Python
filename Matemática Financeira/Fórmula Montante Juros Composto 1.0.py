# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 19:12:40 2019

@author: Caio
"""
    
# Importando a biblioteca pandas
import pandas as pd

#Importando da biblioteca pandas, as ferramentas Series e DataFrame
from pandas import Series, DataFrame

# Calcular o montante de forma simples (ok)
# Exibir o montante na tela (ok)
# Cria uma lista que coloca os aportes e o crescimento do montante em duas séries


#Criando um DataFrame vazio para ser preenchido
df = pd.DataFrame=()

#Contador
i = 0 

#Séries que vão armazenar os valores
aportes=pd.Series([])
tempos=pd.Series([])
taxadejuros=pd.Series([])
Montantes=pd.Series([])

#Variáveis
# Variável Aporte Inicial
C = float(input('insira o valor a ser aplicado inicialmente'))
#Variável Tempo percorrido
t = int(input('insira a quantidade de meses que esse investimento renderá'))
# variável taxa de juros
j = float(input('Insira a taxa de juros para o investimento'))
# montante final
M = C * ((1+(j/100))**t)


while ((i)<(t)):    
    
    aportes.append(C) #Anexa o valor do aporte na série de Aportes
    tempos.append(i) #Insere mais um tempo decorrido dentro da série
    taxadejuros.append(j) #Insere a taxa de juros na série do DataFrame
    Montantes.append(M) #Insere os montantes na série do DataFrame
    i=i+1

df = pd.DataFrame({'Aportes':aportes,'Tempo':tempos,'Taxa de Juros':taxadejuros,'Montantes':Montantes})
df