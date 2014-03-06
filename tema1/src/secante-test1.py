from math import *
def f(x): return 2*log(x)-x+1
res = secante(f, x0=3.0, x1=4.0, tol=1e-6, verb=True)
print "Resultado:", res
