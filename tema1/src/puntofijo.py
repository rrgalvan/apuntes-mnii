def punto_fijo(g, x0, tol=1e-10, maxIters=100, verb=False):
    """Calcula un punto fijo de $g$ partiendo de x0
    
    Args:
       g: Función
       x0: Inicialización del método de aproximaciones sucesivas
       tol: Tolerancia (fin si $|x_{n+1}-x_n|$<tol)
       maxIters: Número máximo de iteraciones permitidas
       verb: Modo verboso activo/inactivob

    Returns:
       c: Aproximación del cero de $f$
       iter: Número de iteraciones realizadas
    """
    iter = 0
    diferencia = tol # Nos aseguramos de entrar en el bucle
    while diferencia >= tol and iter < maxIters:
        # Método de aproximaciones sucesivas
        x1 = g(x0)
        # Preparar siguiente iteración
        diferencia = abs(x1 - x0)
        x0 = x1
        iter = iter + 1        
        # Mostrar información (si se seleccionó el modo verboso)
        if verb: 
            print "Iter", iter, ", x1 =", x1, ", diferencia =", diferencia
    return x1, iter

