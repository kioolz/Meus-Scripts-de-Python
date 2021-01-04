# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 00:04:29 2019

@author: Caio
"""


import pandas as pd
from pandas import DataFrame, Series

Geometriamolecular=pd.Series(["Linear", "Angular", "Piramidal", "Tetraédrica", "Trigonal Plana"])

NomedaMolecula=pd.Series(["Gás Carbônico", "Dióxido de Enxofre","Trióxido de Enxofre","Ozônio",
                          "Amoníaco", "Nitrato", "Trifluoreto de Boro"])

Símbolodamolecula=pd.Series(["CO\N{Subscript Two}", "SO\N{Subscript Two}", "SO\N{Subscript Three}","O\N{Subscript Three}",
                             "NH\N{Subscript Three}","NO\N{Subscript Three}-", "BF\N{Subscript Three}"])

df = pd.DataFrame ( {"Nome da Molécula": NomedaMolecula, "Símbolodamolecula": Símbolodamolecula})


df.loc[[0], 'Geometria da molécula'] = Geometriamolecular[0]
df.loc[[1], 'Geometria da molécula'] = Geometriamolecular[1]
df.loc[[2], 'Geometria da molécula'] = Geometriamolecular[4]
df.loc[[3], 'Geometria da molécula'] = Geometriamolecular[1]
df.loc[[4], 'Geometria da molécula'] = Geometriamolecular[2]
df.loc[[5], 'Geometria da molécula'] = Geometriamolecular[4]
df.loc[[6], 'Geometria da molécula'] = Geometriamolecular[4]




df

df.loc[[7], 'Nome da Molécula'] = "Água"
df.loc[[7], 'Geometria da molécula'] = "H\N{Subscript Two}O"
df.loc[[8], 'Nome da Molécula'] = "Metano"
df.loc[[8], 'Geometria da molécula'] = "CH\N{Subscript Four}"
df.loc[[9], 'Nome da Molécula'] = "Água"
df.loc[[10], 'Nome da Molécula'] = "Água"
df.loc[[11], 'Nome da Molécula'] = "Água"
df.loc[[12], 'Nome da Molécula'] = "Água"


