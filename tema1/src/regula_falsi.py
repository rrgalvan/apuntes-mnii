def regula_falsi(f, a, b, tol=1e-10, maxIters=100, verb=False):
    """Calcula una raíz de $f(x)=0$ mediante el método de 'regula falsi'

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
    diferencia = tol # Nos aseguramos de entrar en el bucle
    while diferencia>=tol and iter < maxIters:
        # Mostrar información (si se seleccionado el modo verboso)
        if verb: print "Iter", iter, ", [a, b] = [", a, ", ", b,
        # Calcular el punto medio
        c = b - f(b)*(b-a)/(f(b)-f(a)); fc = f(c)
        diferencia = min(b-c, c-a)
        print "], dif =", diferencia
        # Calcular el nuevo subintervalo e iterar
        if fa*fc < 0:
            b=c; fb=fc; 
        else:
            a=c; fa=fc  
        iter = iter + 1
    return c, fc, iter

