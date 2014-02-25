from math import *
def g(x): return sqrt(sin(x)+1)
x0 = 1
res = punto_fijo(g, x0, tol=1e-5, verb=True)
print "Resultado: ", res
