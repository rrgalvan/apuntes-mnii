from math import *
def f(x): return 2*log(x)-x+1
def df(x): return (2-x)/x
res = newton(f, df, x0=3.0, tol=1e-6, verb=True)
print "Resultado:", res
