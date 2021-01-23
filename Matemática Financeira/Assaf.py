# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:03:50 2019

@author: Caio
"""
# Livro Assaf - Mercado Financeiro
#Capítulo 7.6.1 - Desmembramento da taxa básica de juros

i_pura = float(input('Insira a taxa livre de risco da economia'))
i_risco = float(input('Insira a taxa de risco mínimo da economia'))
i_real = float
i_real = (1+i_pura) * (1+i_risco)-1
print = (' A taxa real de juros para esta operação é:', i_real)
INF = float(input('Insira a taxa de inflação do período'))

SELIC = float
SELIC = (1 + i_real) * (1 + INF) - 1
print(SELIC)

