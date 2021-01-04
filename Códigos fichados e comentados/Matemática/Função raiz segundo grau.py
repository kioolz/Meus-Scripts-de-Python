# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:37:26 2019

@author: Caio
"""


#---------------------------------------------------------------------------------------------

#Exemplo de função de segundo grau com os parâmetros definidos ---
# Próximo passo é colocar um botão para o usuário definir cada parâmetro da variável
# Colocar um comando que printe o gráfico da função de segundo grau.

#Os três métodos funcionam - Preciso de uma estrutura condicional para que o Delta funcione. 



from math import sqrt

a=float(input('Insira o valor do coeficiente A'))
b=float(input('Insira o valor do coeficiente B'))
c=float(input('Insira o valor do coeficiente C'))

y1=(-b+(b*b-4*a*c)**0.5)/(2*a)
y2=(-b-(b*b-4*a*c)**0.5)/(2*a)

y1a=2*c/(-b-sqrt(b*b-4*a*c))
y2a=2*c/(-b+sqrt(b*b-4*a*c))
print('Raiz 1 =', y1, 'Raiz 1 alternativa=' , y1a)
print('Raiz 2 =', y2, 'Raiz 2 alternativa=' , y2a)


#--------------------------------------------------------------------------------------#

from math import sqrt

a=float(input('Insira o valor do coeficiente A'))
b=float(input('Insira o valor do coeficiente B'))
c=float(input('Insira o valor do coeficiente C'))

y1=(-b+sqrt(b*b-4*a*c))/(2*a)
y2=(-b-sqrt(b*b-4*a*c))/(2*a)

y1a=2*c/(-b-sqrt(b*b-4*a*c))
y2a=2*c/(-b+sqrt(b*b-4*a*c))
print('Raiz 1 =', y1, 'Raiz 1 alternativa=' , y1a)
print('Raiz 2 =', y2, 'Raiz 2 alternativa=' , y2a)

#---------------------------------------------------------------------------------------#

from math import sqrt

a=float(input('Insira o valor do coeficiente A'))
b=float(input('Insira o valor do coeficiente B'))
c=float(input('Insira o valor do coeficiente C'))

y1 = ((b*(-1)) + sqrt(b*b-4*a*c)) / (2 * a)
y2 = ((b*(-1)) - sqrt(b*b-4*a*c)) / (2 * a)

y1a=2*c/(-b-sqrt(b*b-4*a*c))
y2a=2*c/(-b+sqrt(b*b-4*a*c))
print('Raiz 1 =', y1, 'Raiz 1 alternativa=' , y1a)
print('Raiz 2 =', y2, 'Raiz 2 alternativa=' , y2a)
