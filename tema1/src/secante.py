def secante(f, x0, x1, tol=1e-10, maxIters=100, verb=False):
    """Calcula una raíz de $f(x)=0$ mediante el método de la secante.

    Args:
       f: Función
       x0: Primera estimación de la solución
       x1: Segunda estimación de la solución
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
        # Método de la secante
        x2 = x1 - f(x1)* (x1-x0)/(f(x1)-f(x0))
        # Preparar siguiente iteración
        diferencia = abs(x1 - x0)
        x0 = x1
        x1 = x2
        iter = iter + 1        
        # Mostrar información (si se seleccionó el modo verboso)
        if verb:
            print "Iter %d, x_%d=%1.10g, dif=%g" % (iter, iter, x2, diferencia)
    return x2, iter
