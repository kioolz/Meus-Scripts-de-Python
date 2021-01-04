

#Linha de Código que cria uma sequência dos inteiros positivos maiores que 0
# 0 Demonstra o conjunto vazio.
V = True
while V==True:
    list(map(lambda i: print(i, end=''), [i for i in range(1, int(input()) + 1)]))
    
    
