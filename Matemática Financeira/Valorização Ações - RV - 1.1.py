# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:51:31 2019

@author: Caio
"""

#Importando os módulos para escrever as séries e DataFrames
import pandas as pd
from pandas import DataFrame, Series
from datetime import date


#Criando uma variável para a data de hoje.
#Esta variável futuramente vai entrar no date range para ir contando os dias, dentro do DataFrame
# De forma que eu possa preencher com as informações da web o que acontece com cada uma das ações.
datas = date.today()
datas

#Também posso usar o comando datetime.now para modificar o dataframe no intervalo de tempo que eu desejar.

import datetime 
datetime.datetime.now()


# Inserindo uma variável que controla os intervalos de tempo de acordo com os dias
datasrange = pd.date_range('2019-09-21', '2019-12-31', freq='D')
datasrange



#Criando uma série com os nomes das ações para serem o index
#Esta tupla contém as siglas dos capitais aonde tem dinheiro investido
# Posso trocar esta tupla por um dicionário e tentar preencher com mais informações
siglas = Series(['ABEV3F', 'IGTA3F', 'ITSA4F', 'MRVE3F', 'EGIE3F'])
siglas


#Criando uma série com as quantidades de cada uma das ações
Quantidade = Series([8,3,10,7,2])
Quantidade

#Valor pago por ação
ValorPago = Series ([18.08, 44.8, 11.98 , 17.9 , 42.48])
ValorPago

#Montante Inicial gasto nas ações
MontanteInicial = Series ([144.64 , 134.4, 119.8, 125.3 , 84.96])
MontanteInicial

#Valor Atual
ValorAtual = Series([19.42, 47.29 , 13.14 , 18.3 , 44,89])
ValorAtual

#MontanteFinal das ações pós valorização ou desvalorização
MontanteFinal = Series([155.28, 142.32, 131.8, 128.59 , 90.2])
MontanteFinal

# Inserindo a Taxa de Corretagem da financeira
TaxadeCorretagem = Series([7.5 , 7.5, 7.5 , 7.5 , 7.5])

#Inserindo a variável Lucro para a contabilização das ações.
LucroLiquido = MontanteFinal - MontanteInicial - TaxadeCorretagem
LucroLiquido

#Valorização da Ação
Valorização = ValorAtual - ValorPago
Valorização


# Criando um df aonde serão inseridos todos os valores das ações
df_acoes = DataFrame({'siglas': siglas, 'Quantidade': Quantidade, 'Valor Pago' : ValorPago,
                      'Montante Inicial': MontanteInicial, 'Montante Final': MontanteFinal, 
                      'Lucro Líquido': LucroLiquido, 'Valorização': Valorização})


df_acoes
# Agora preciso extrair as informações de cada uma das ações e usar seus valores numéricos
# para analisar outras ações.


