
# Importando arquivos do tipo CSV para o Python, lendo DataFrames do Excel..
import pandas as pd



# Colocando os diretórios das pastas e dos arquivos no formato CSV e na criptografia Latin1

df2 = pd.read_csv("C:\\Users\\Caio\\Desktop\\Python Scripts\\Planilha 2.csv", encoding='latin1')
df3 = pd.read_csv("C:\\Users\\Caio\\Desktop\\Python Scripts\\CSV1.csv")

#Exibe os dataframes
df = pd.read_csv("C:\\Users\\Caio\\Desktop\\Python Scripts\\Planilha 1.csv", encoding='latin1')
df
df2
df3


#Exibe o tipo de variável dentro do dataframe.
df.dtypes