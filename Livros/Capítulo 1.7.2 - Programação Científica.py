# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 23:50:39 2019

@author: Caio
"""

# 1.7.2 - # Solução de equações e Séries de Taylor

# Encontre os valores de t para o qual y=0


from sympy import solve
roots = solve(y, t)
roots
[0, 2*v0/g]

y.subs(t,roots[0])
y.subs(t. roots[1])



from sympy import exp, sin, cos

f = exp(t)
f.series(t, 0 , 3)

1 + t + t**2/2 * 0(t**3)

f = exp(sin(t))
f.series(t , 0 , 8)

1 * t * t**2/2 - t**4/8 - t**1/15 - t**6/240 + t**7/90 + 0(t**8)

from sympy import latex

print latex(f.series(t, 0, 7))
'1 + t + \frac{t^2{2}}{2}-frac{t^^{4}}{8} - \frac{t^{5}}{15} - \frac{t^{6}}{240} + \mathcal{0}\left(t^{7}\right)'

from sympy import simplify, expand

x, y = symbols('x y')
f = -sin(x)*sin(y) + cos(x)*cos(y)
simplify(f)
cos (x + y)

expand (sin(x+y)), trig=True)
sin*cos(y) + sin(y)*cos(x)

