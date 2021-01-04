# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:19:59 2019

@author: Caio
"""

#Criando um DataFrame básico envolvendo 2 vetores de 2 dimensões.

import numpy as np
import pandas as pd


# Criando um dataframe que cria uma matriz 2x2 ou 2 vetores de 2 dimensões
#Adicionando nome para as colunas da matriz e exibindo elas na tela

df = pd.DataFrame(np.array([[10,11] , [20,21]]), columns = ['a' , 'b'])

df








#Organizando os termos de um DataFrame básico em ordem crescente

df1 = pd.DataFrame ([pd.Series(np.arange(10,15)), pd.Series(np.arange(15,20))])

df1

# Calcula as dimensões da matriz formada pelo DataFrame

df1.shape