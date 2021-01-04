# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:49:56 2019

@author: Caio
"""

# Densidade relativa dos gases
#A densidade absoluta ou massa específica de um gás, em determinada pressão e temperatura, é o quociente
#entre a massa e o volume do gás.
#Se o volume do gás for idêntico, podemos dizer que a densidade do gás é igual sua massa
# Se houvermos uma mistura de diversos gases, a densidade relativa entre eles é a razão entre suas densidades.
#nas condições consideradas de pressão e temperatura temos




class DensidadeAbsolutaeRelativa:
   
    
    
    def DensidadeAbsoluta():
        
        
        #Define as listas que vão colher as informações de cada amostra
        densidadedecadaamostra=[]
        massadecadaamostra=[]
        volumedecadaamostra=[]
        DensidadesRelativasdaMistura=[]
        
        #Contador para iniciar o programa
        i=1
        
        
        #Total de amostras inseridas pelo usuário para a análise e armazenada na variável totaldeamostras
        print ("Quantas amostras você tem para comparar a densidade?")
        totaldeamostras=int(input())
        
        
        #Se o total de amostras é maior que 0 , o programa inicia.
        if (totaldeamostras > 0):
            
            # O programa roda na condição estabelecida pelo total de amostras.
            for i in range (0, totaldeamostras):
                             
                #Insere as massas ao longo do contador i
                print("Insira o valor da massa", (i+1), "\n")
                Massa=float(input()) # Massa é um valor real
                print("O Valor inserido para a massa", (i+1)," foi : ", Massa, "\n")
                #Daqui seria necessário colocar uma condicional caso o usuário erre, mas isso fica pra versão 1.3
                
                massadecadaamostra.append(Massa)
        
                # Mesma lógica que a massa
                print ("Insira o valor do volume", (i+1), "\n")
                Volume=float(input())
                print("O volume inserido para o volume", (i+1), "foi : ", Volume, "\n")
                volumedecadaamostra.append(Volume)
                
                
                
                densidade=Massa/Volume
                print("Esta é a densidade da amostra",(i+1), "é:", densidade, "\n")
                densidadedecadaamostra.append(densidade)
                
                
                
                print("Esta são as densidades de cada amostra", densidadedecadaamostra)
                
                
                densidaderelativa=densidadedecadaamostra[i-1]/densidadedecadaamostra[i]
                i=i+1
                DensidadesRelativasdaMistura.append(densidaderelativa)
                print("Esta é a densidade relativa desta etapa em relação a anteior:", densidaderelativa)
                
                print ("Esta é a densidade relativa de cada etapa da amostragem: ", DensidadesRelativasdaMistura)
            
        
            
    DensidadeAbsoluta()


    
