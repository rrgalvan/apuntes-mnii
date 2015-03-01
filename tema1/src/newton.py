def newton(f, df, x0, tol=1e-10, maxIters=100, verb=False):
    """Calcula una raíz de $f(x)=0$ mediante el método de Newton

    Args:
       f: Función
       df: Función derivada
       x0: Inicialización del método de Newton
       tol: Tolerancia
       maxIters: Número máximo de iteraciones permitidas
       verb: Modo verboso activo/inactivo

    Returns:
       c: Aproximación del cero de $f$
       iter: Número de iteraciones realizadas
    """
    iter = 0
    diferencia = tol # Nos aseguramos de entrar en el bucle
    while diferencia >= tol and iter < maxIters:
        # Método de Newton
        x1 = x0 - f(x0)/df(x0)
        # Preparar siguiente iteración
        diferencia = abs(x1 - x0)
        x0 = x1
        iter = iter + 1        
        # Mostrar información (si se seleccionó el modo verboso)
        if verb:
            print "Iter %d, x_%d=%1.10g, dif=%g" % (iter, iter, x1, diferencia)
    return x1, iter
