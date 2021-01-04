# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:19:39 2019

@author: Caio
"""

import pandas as pd
from pandas import Series, DataFrame

Moléculas=pd.Series(['CO2','O2','CH4','H2S','CCl4','H2O','SO2','NaCl','HCl','Cl2'])
Polaridade=pd.Series(['Apolar','Apolar','Apolar','Polar','Apolar','Polar','Polar','Polar','Polar','Apolar'])
GeometriaMolecular=[]

df=pd.DataFrame({'Moléculas':Moléculas,'Polaridade':Polaridade})
df






