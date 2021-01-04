# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:55:34 2019

@author: Caio
"""

#Código que cria um dicionário que serve para armazenar o nome e a fórmula química de ácidos.


#Módulo Pandas para manipular dados String/Int/Float em um mesmo DataFrame
import pandas as pd
from pandas import Series,DataFrame



# Série do Pandas que contém os nomes dos ácidos, essa vai ser a coluna que contém estes nomes.
    NomesdosÁcidos=pd.Series(["Ácido Permangânico", "Ácidos Fosforoso",
                              "Ácido Oxálico", "Ácido Sulforoso",
                              "Ácido Arsênico",
                              "Ácido ortossilícico", "Ácido Fosfórico", "Ácido nitroso", "Ácido nítrico",
                              "Ácido hipofosforoso", "Ácido pirofosfórico",
                              "Ácido cloroso",
                              "Ácido perlórico", "Ácido clórico","Ácido Sulfúrico"])
    NomesdosÁcidos # Chama a série com os nomes
    
    
    #Dicionário com as fórmulas
    FórmulasdosÁcidos=pd.Series(["H\N{Subscript Three}PO\N{Subscript Three}",
                                 "HMnO\N{Subscript Four}", 
                                 "H\N{Subscript Two}C\N{Subscript Two}O\N{Subscript Four}",
                                 "H\N{Subscript Two}SO\N{Subscript Three}",
                                 "H\N{Subscript Three}AsO\N{Subscript Four}",
                                 "Si(OH)\N{Subscript Four}"])
    FórmulasdosÁcidos # Chama as fórmulas
    
    
    
    # Data Frame que concatena as linhas e colunas dos ácidos
    df = DataFrame({"Nomes dos Ácidos": NomesdosÁcidos, "Fórmulas dos Ácidos": FórmulasdosÁcidos})
    
    df


    df.isnull() # Mostra quantos elementos estão faltando no dataFrame
    df.isnull().sum() # Soma a quantidade de elementos faltantes em cada coluna
    df.loc[[6], 'Fórmulas dos Ácidos'] = 'H\N{Subscript Three}PO\N{Subscript Four}'
    df.loc[[7], 'Fórmulas dos Ácidos'] = 'HNO\N{Subscript Two}'
    df.loc[[8,9], 'Fórmulas dos Ácidos'] = 'HNO\N{Subscript Three}', 'H\N{Subscript Three}PO\N{Subscript Two}'
    df.loc[[10], 'Fórmulas dos Ácidos'] = 'H\N{Subscript Four}P\N{Subscript Two}O\N{Subscript Seven}'
    df.loc[[11,12,13, 14], 'Fórmulas dos Ácidos'] = 'HClO\N{Subscript Two}','HClO\N{Subscript Four}','HClO\N{Subscript Three}','H\N{Subscript Two}SO\N{Subscript Four}'
    
    df