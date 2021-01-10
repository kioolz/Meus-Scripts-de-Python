# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:55:23 2019

@author: Caio
"""

import pandas as pd
import datetime
import numpy as np


date_range = pd.date_range(start='11/10/2019', end='31-12-2019',freq='D') #Estabelecendo a frequência com que a série temporal vai percorrer, a frequência em Dias.

df = pd.DataFrame(date_range, columns=['date']) #Criando um dataframe onde as colunas são o intervalo do Date


