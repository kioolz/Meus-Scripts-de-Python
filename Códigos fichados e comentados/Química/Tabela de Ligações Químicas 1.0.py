# -*- coding: utf-8 -*-


import pandas as pd
from pandas import DataFrame,Series






Compostos=pd.Series(['Tribrometo de Fósforo', 'Iodeto de Potássio','Bicarbonato de Sódio','Cloreto de Amónio','Ureia'])
Símbolo=pd.Series(['PBR\N{Subscript Three}','KI','NaHCO\N{Subscript Three}','NH\N{Subscript Four}Cl','CO(NH\N{Subscript Two})\N{Subscript Two}'])
TiposdeLigações=pd.Series(['Covalente','Iônica','Hidrogênio'])
df=DataFrame({'Compostos':Compostos,'Símbolo':Símbolo, 'Tipos de ligação':TiposdeLigações})
df.loc[[0,1,2,3,4], 'Tipos de ligação'] = 'Covalente', 'Iônica', 'Iônica', 'Covalente','Covalente'
df


