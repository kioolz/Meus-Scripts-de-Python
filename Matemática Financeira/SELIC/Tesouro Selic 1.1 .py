# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:59:00 2019

@author: Caio
"""

# Importando as biblitoecas necessárias

import pandas as pd
import numpy as np
import matplotlib as plt

from pandas import DataFrame,Series
from datetime import datetime

# Bom, eu fiz 2 aportes no tesouro SELIC. 
# O objetivo deste código é preencher um dataframe com uma coluna de DateTimes 
#para efetuar uma operação de rendimento líquido deste tesouro
# Onde a partir desses datetimes diários, eu preencha colunas de um dataframe com os rendimentos associados aos aportes
# E outra lista associando as datas das compras aos aportes

# ---- Variáveis ---- 

# Criei um range de datas do dia do meu primeiro aporte até o último dia que vence este tesouro SELIC

# Inseri uma lista com as datas dos aportes
datasdecompra = ['21/08/2019', '02/09/2019']
#Uma lista com os valores dos aportes.
valoresdosaportes = [4971.52, 2071.47]
#Taxa Selic
taxaselic=(5.5/36500) #  ( 5.5/100 ) 365 para transformar de ano para dia
# Com isso, posso começar as operações de rendimento desses valores.

IR1=22.5/100
IR2=20/100
IR3=17.5/100
IR4=15/100


#O dataframe com as datas como uma coluna 
df = pd.DataFrame(dates)
df
# While Datetime é diferente '01/03/2025' , execute

