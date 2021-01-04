
# Calendário - Deve seguir os seguintes critérios

# 1 -- O Ano sempre pode ser dividido por 4 é um ano Leap. 
# 1.1 -- A menos que : O ano sempre possa ser dividido por 100
# - Então ele não é um ano leap


# 1.2 -- Ele também pode ser dividido por 400, se for, é um ano leap. 



def is_leap(year):
    leap=False  
    # Escreva a lógica para criar o ano bissexto
    if (year) % 4 == 0:
        leap=True
    else:
        leap=False
    if (year) % 100 ==0:
        leap=False
    if (year) % 400 ==0:
        leap=True
    return leap


year = int(input())
