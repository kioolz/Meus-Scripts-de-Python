# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 16:03:47 2019

@author: Caio
"""


import pandas as pd


TabeladePosicoes=[]
TabeladeTempos=[]

while (len(TabeladePosicoes)<5) and (len(TabeladeTempos)<5):
    print("Insira uma posicao")
    X=float(input())
    TabeladePosicoes.append(X)
    print("Insira um tempo")
    T=float(input())
    TabeladeTempos.append(T)
    
ExibeTabela = pd.DataFrame(TabeladePosicoes, TabeladeTempos)

print (ExibeTabela)

