from math import *
g = lambda x: sqrt(sin(x)+1)
res = punto_fijo(g, x0=1.0, tol=1e-5, verb=True)
print "Resultado: ", res
