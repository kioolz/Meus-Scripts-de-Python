# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 12:26:35 2019

@author: Caio
"""

def newton_method(number, number_iters = 500):
    a = float(number) # number to get square root of
    for i in range(number_iters): # iteration number
        number = 0.5 * (number + a / number) # update
	  # x_(n+1) = 0.5 * (x_n +a / x_n)
    return number

print (newton_method(9))
print (newton_method(2))
