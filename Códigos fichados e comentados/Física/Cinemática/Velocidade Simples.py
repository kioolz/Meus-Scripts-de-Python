# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:18:13 2019

@author: Caio
"""
#-----------------------------#-----------------------------#-----------------------------#-----------------------------
 # Modificações realizadas -     

!pip install matplotlib


#Definimos uma variável para iniciar o contador de quantos valores serão inseridos
 #Enquanto esta variável permanecer ligada, ele vai acrescentar mais dados para a lista.
V=True

#Variáveis booleanas que servirão para definir a estrutura que repete o código ou para o código
#Em implementação, a estrutura do If ainda não funciona bem.
Sim=True
Não=False

#Listas que irão armazenar as variáveis associadas a X, Xo, T, To e Vel
PosiçõesFinais=[]
PosiçõesIniciais=[]
TemposFinais=[]
TemposIniciais=[]
VelocidadesMédias=[]
#Estrutura condicional para criar o loop
while V!=False:  
    #Série de Comandos que permite o usuário colocar as variáveis físicas do problema
    print ("Insira seu deslocamento em relação a origem")
    X = float(input())
    PosiçõesFinais.append(X)
    print ("Insira o ponto de origem")
    Xo = float(input())
    PosiçõesIniciais.append(Xo)
    print ("Insira o tempo final")
    T = float(input())
    TemposFinais.append(T)
    print ("Insira o tempo inicial")
    To = float(input())
    TemposIniciais.append(To)
    Vel = [(X-Xo)/(T-To)]
    VelocidadesMédias.append(Vel)
    print("Sua velocidade média foi", Vel, "m/s")
    print ("Esta é a lista com as posições finais", PosiçõesFinais)
    print ("Esta é a lista com as posições iniciais", PosiçõesIniciais)
    print ("Esta é a lista com os tempos finais", TemposFinais)
    print ("Esta é a lista com os tempos iniciais", TemposIniciais)
    print ("Sua velocidade média durante o percurso foi", VelocidadesMédias)
    break
#Importando as bibliotecas gráficas
import matplotlib.pyplot as plt
import numpy as np
grafico = plt.figure(Vel) #Cria um gráfico sem eixos, vazio
grafico.suptitle("não tem eixo neste gráfico")
grafico, ax_lst = plt.subplots(1,1) #Uma figura com 2x2 divisões
    
    


    








