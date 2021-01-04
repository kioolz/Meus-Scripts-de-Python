# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 22:07:33 2019

@author: Caio
"""

# Exemplo de Matriz 2 x 3 

A = [[ 1, 2, 3], [4,5, 6]]

# Exemplo de Matriz 3 x 2 

B = [[1,2], [3,4], [5,6]]

def shape (A):
    num_rows = len(A)
    num_cols= len(A[0]) if A else 0 # Número de elementos na primeira linha
    return num_rows, num_cols



def get_row( A, i): 
    return A[i]     #A[i] já é da linha A[i] é linha i-ésimo
def get_column (A, j):
    return [A_i[j] for A_i in A] #J-ésimo elemento da linha A_i para cada linha A_i


def make_matrix(num_rows,num_cols,entry_fn):
    """Retorna a matriz num Rows X num_cols cuja entrada (i,j) th é entry_fn (i,j) """
    return[[entry_fn(i,j) 
    for j in range(num_cols)
    for i in range(num_rows)]






    