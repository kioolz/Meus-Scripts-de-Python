# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:28:23 2019

@author: Caio
"""


#Importando a biblioteca Pandas e o registro do tempo para o Python

import pandas as pd
from datetime import date
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

# Criando uma série no pandas que represente a indexação das linhas como valores temporais
# Por exemplo, datas do calendário do ano.


dates = pd.date_range(start='11-10-2019', end='31-12-2019') #Intervalo de tempo do DateTime
dates
#O que faço com esse index Dates?
#

#Criando um dataframe de uma linha e uma coluna, ou uma série. 
#renomeando as linhas ou índices i da série ou matriz ou dataframe (df) através do comando 'index'
# Acrescentando a série de datas a Série numérica criada. 
#E Agora vamos inserir variáveis reais ao problema
#inserindo a variável Montante inicial como uma série numérica
MontanteInicial=pd.Series([6986.16, 6986.16, 6986.16, 6986.16, 6986.16], index = dates)
MontanteInicial

#Repetindo o processo para os valores ganhos diariamente em relação ao dia anterior.
#Podemos construir uma tabela de valores que apresente o lucro diário em relação ao dia anterior
MontanteFinal =pd.Series([6990, 6991, 6994, 6998, 7000], index = dates)
MontanteFinal

#Operação de subtração entre as componentes da lista - Criando através da operação, uma lista
#que me diz quanto lucrei no total. 
#Calculando a diferença entre os índices da matriz/Dataframe e plotando a resposta no próprio DF.
LucroTotal = MontanteFinal-MontanteInicial
LucroTotal

# E com a operação feita, posso associar a tabela o valor da Taxa Selic em cada dia e alterar como conforme a necessidade.
TaxaSelic = pd.Series(['5.5%', '5.5%', '5.5%', '5.5%', '5.5%'], index = dates)

#Criando um DataFrame que usa como colunas, duas séries que representam numeros aleatórios associado a duas possiveis variáveis.
df_temp =pd.DataFrame({'Montante Final': MontanteFinal, 'Montante Inicial': MontanteInicial, 'Taxa Selic': TaxaSelic, 'Lucro Total' : LucroTotal})
df_temp





