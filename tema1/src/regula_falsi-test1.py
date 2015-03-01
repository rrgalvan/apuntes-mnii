from math import *
def f(x): return 2*log(x)-x+1
res = regula_falsi(f, 3.0, 4.0, tol=1e-6, verb=True)
print "Resultado:", res
