def f(x): 
    return x**3 - 9*x + 3
a, b = 0, 1
res = biseccion(f, a, b, tol=1e-2, verb=True)
print "Resultado: ", res
