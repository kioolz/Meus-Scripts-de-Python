# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:31:57 2019

@author: Caio
"""


# Exercício com a biblioteca pandas

# O objetivo é criar uma série de Tabelas que organizam os alimentos da casa


# Bugado, diz que as matriz precisam ter o mesmo comprimento
import pandas as pd
from pandas import DataFrame, Series


    def Alimentação():
    
        Comida=pd.Series(['Arroz', 'Feijão'])
        Grãos=pd.Series(['Arroz', 'Feijão', 'Lentilha','Aveia'])
        Frutas=pd.Series(['Laranja','Limão','Banana','Morango','Maracujá','Pêssego'])
        Carnes=pd.Series(['Boi','Frango','Porco'])
        Alimentos = pd.DataFrame({'Grãos': Grãos,'Frutas': Frutas,'Carnes': Carnes})

    Alimentação()




#Preciso de uma estrutura que organize os grãos, as frutas e os carboidratos
# E preencha suas entradas num dicionário.
