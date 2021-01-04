# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:10:23 2019

@author: Caio
"""

#-----------------------------------------------------------------------------
# Teste, exibir o Salário de um trabalhador em uma empresa

def main():

    Dias = int(input('Numero de Dias Trabalhados :'))
    Horas = int(input('Numero de Horas trabalhadas:'))
    ValorPorHora = int(input('Digite o quanto você ganha por hora:'))
    SalarioMensal = Dias*Horas*ValorPorHora
    print ("O empregado trabalhou",Dias,"dias", "Totalizando", Horas,"Horas mensais", "e recebeu",
           ValorPorHora,"por cada hora de trabalho")
    print("Seu salario neste mês foi", SalarioMensal)
    
    
#------------------------------------------------------------------------------
# Agora vamos comparar o salário dos trabalhadores 
    
    if (SalarioMensal > 5000) and (SalarioMensal <= 10000):
        print ('Este funcionario ganha entre 5 a 10 salarios minimos')
    else:
        print('Este funcionario ganha abaixo de 5 salario minimos ou acima de 10 salarios minimos')
#-----------------------------------------------------------------------------

# Próximas modificações : Adicionar um While para contar a quantidade de trabalhadores na empresa
# Atribuir a cada trabalhador seu respectivo salário
#Comparar o salário dos trabalhadores
#Tentar agrupar a quantidade de trabalhadores de acordo com suas faixas salariais
        
    
main()



def main():
    
    nome = input('Qual o seu nome?')
    idade = int(input('Quantos anos você tem?'))
    peso = float(input ('Quantos quilos você tem?'))
    print ("Seu nome e", nome,"Sua idade e ", idade,"Seu peso e", peso)
    
main()




