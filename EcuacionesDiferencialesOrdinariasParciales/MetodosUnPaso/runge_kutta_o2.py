import math
import numpy as np

def runge_kutta_orden2_func(f_str, x0, y0, h, n):
    # Preparar contexto seguro para evaluar funciones
    contexto = {
        **{func: getattr(math, func) for func in dir(math) if callable(getattr(math, func))},
        "np": np
    }

    # Crear la función f(x, y)
    f = lambda x, y: eval(f_str, contexto, {"x": x, "y": y})

    x, y = x0, y0
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y = y + (h / 2) * (k1 + k2)
        x = x + h

    y_final = round(y, 4)

    return {
        "y_final": y_final,
        "mensaje": f"El valor final de y después de {n} iteraciones es: {y_final:.4f}"
    }