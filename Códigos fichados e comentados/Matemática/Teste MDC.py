# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:54:00 2019

@author: Caio
"""

i = 0

for i in range (0, 4):
    A = int(input())
    B = int(input())
    MDC = float
    anterior = A
    atual = B
    resto = (anterior%atual)
    def min (A,B):
        if B<= A:
            return A
        else:
            return B
    def max(A,B):
        if A<= B:
            return B
        else:
            return A
    if B==0:
        MDC = A
    else:
        MDC = resto
    
    print (A,B, MDC)
    print (A)
    print (B)
    print (min)
    print (max)
        