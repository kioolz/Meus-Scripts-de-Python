# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:29:07 2019

@author: Caio
"""

# Adicionando o ID Dos usuários e seus respectivos Nomes
from __future__ import division

users = [{ "id": 0, "name": "Hero"}, 
         { "id": 1, "name": "Dunn"},
         {"id": 2, "name": "Sue"}, 
         {"id": 3, "name": "Chi"}, 
         {"id": 4, "name": "Thor"},
         {"id": 5, "name" : "Clive"},
         {"id":6 , "name" : "Hicks"},
         {"id": 7, "name" : "Devin"}, 
         {"id": 8, "name" : "Kate"}, 
         {"id": 9, "name" : "Klein"}]
#Co -relação das amizades entre os funcionários 
friendships = [(0,1),(0,2),(1,2),
               (1,3), (2,3), (3,4), 
               (4,5), (5,6), (6,8),
               (7,8), (8,9)]
# Adicionar a uma lista de amigos para cada usuário.
# Configuramos a propriedade Friends    de cada usuário em uma lista vazia
#Adicionar os usuários a uma lista Vazia de amigos.
#Lista com os dados de amizade - 
for user in users:
    user["friends"]=[]
    
    for i,j in friendships:
        users[i]["friends"].append(users[j]) # Adiciona i Como amigo de J
        users[j]["friends"].append(users[i]) # ADiciona J como amigo de I           
        
#AGora vou encontrar o máximo de conexões possíveis 
def number_of_friends(user):
    """Quantos amigos o usuário tem?"""
    return len(user["Friends"]) # Tamanho da Lista de Amigos
total_connections = sum(number_of_friends(user) for user in users)


# Então dividimos pelo número de usuários   
 #Divisão inteira está incompleta
num_users = len(users) #Tamanho da Lista de usuários
avg_connections = total_connections / num_users #2.4

# É or denado pelo numero de amigos, do maior para o menor

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
sorted(num_friends_by_id, key=lambda(user_id,num_friends):num_friends, reverse=True)


def friends_of_friend_ids_bad(user):
    
    return [foaf["id"]
            for friend in user["friends"] #Para cada amigo de usuário
            for foaf in friend["Friends"] # Pega cada _their friends
            
            






