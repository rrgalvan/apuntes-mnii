def biseccion(f, a, b, tol=1e-10, maxIters=100, verb=False):
    """Calcula una raíz de $f(x)=0$ en $(a,b)$ mediante el método de bisección

    Args:
       f: Función
       a, b: Extremos del intervalo,
       tol: Tolerancia
       maxIters: Número máximo de iteraciones permitidas
       verb: Modo verboso activo/inactivo

    Returns:
       c: Aproximación del cero de $f$
       fc: Residuo (valor de $f(c)$)
       iter: Número de iteraciones realizadas
    """
    # Comprobar que hay algún cero en el intervalo
    fa = f(a); fb=f(b)
    assert fa*fb<0
    # Realizar iteraciones
    iter = 0
    while b-a >= tol and iter < maxIters:
        # Mostrar información (si se seleccionado el modo verboso)
        if verb: print "Iter", iter, ", [a, b] = [", a, ", ", b, "]"
        # Calcular el punto medio
        c = (a+b)/2.; fc = f(c)
        # Calcular el nuevo subintervalo e iterar
        if fa*fc < 0:
            b=c; fb=fc
        else:
            a=c; fa=fc  
        iter = iter + 1
    return c, fc, iter

