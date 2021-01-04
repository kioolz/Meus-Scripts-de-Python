

#botão que insere uma variável do tipo inteira pelo usuário
n=int(input())


#Estrutura condicional. 
# % Significa módulo! 
# Se o módulo da operação (N%2) for diferente de 0
if int(n) % 2 !=0:
    #Escreva - Estranho
    print ('Weird')
#Se o módulo da operação (N%2) for igual a 0 e maior que 2 e menor que 5
if int(n) % 2 == 0 and n>=2 and n<=5:    
    #Escreva, não é estranho
    print('Not Weird')
##Se o módulo da operação (N%2) for igual a 0 e maior que 6 e menor que 20
if int(n) % 2 ==0 and n>=6 and n<=20:    
    #Escreva - Estranho
    print ('Weird')
    #Se o módulo da operação N for maior que 2 e não for divisivel por 2 
if n>20 and int(n) % 2==0:
    #Escreva, não é estranho.
    print('Not Weird')

    
