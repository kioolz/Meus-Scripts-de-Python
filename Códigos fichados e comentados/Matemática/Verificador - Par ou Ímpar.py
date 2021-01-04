#Uma característica interessante que define os números Pares e Ímpares
# É que o resto da divisão de um número par é zero
# E o resto da divisão de um numero impar é diferente de 0



#Enquanto esta condição estiver ligada
V = True;
while V ==True:   
    # O usuário insere um número inteiro
    n =int(input())  
    #E verifica que se a divisão deste inteiro por um número par for diferente de zero
    if int(n) % 2 !=0:
        print (n, 'é um número ímpar')
        #O número é impar
    if int(n) % 2 == 0:
        print(n, 'é um número par')
        #O número é par
    
#Se eu trocar a classe Int pela classe Float. 
#Problema 1 -  O código começa a interpretar que os valores com 1 dígito depois da vírgula são todos ímpares
#Errata 1 - Todos os número com qualquer quantidade de dígitos depois da vírgula.
#Possívelmente porque quando se trata de um número real e não inteiro
# Dificilmente o resto da divisão será 0! 
# O que caracterizavia um número impar, porém a propriedade citada no íncio do código
#Vale apenas para os valores inteiros e positivos.
#Problema 2 - O que faz com que o código também não exiba os números negativos e os identifique
        #Como pares ou ímpares , e mesmo sendo negativos, ainda são inteiros e podem
        # ser representados por ímpar ou par no código.
        
    
    

    
    


    





    
