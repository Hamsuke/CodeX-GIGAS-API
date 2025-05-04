import numpy as np

def minimos_cuadrados(sx, sy):
    # Si los valores son cadenas, convertirlos en listas de números
    if isinstance(sx, str):
        sx = [float(valor) for valor in sx.split(",")]
    if isinstance(sy, str):
        sy = [float(valor) for valor in sy.split(",")]

    # Convertir listas a arrays NumPy
    x = np.array(sx, dtype=float)
    y = np.array(sy, dtype=float)

    # Verificar que las listas tienen la misma longitud
    if len(x) != len(y):
        raise ValueError("Las listas de valores de x e y deben tener la misma longitud.")

    # Calcular sumas necesarias
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xx = np.sum(x ** 2)
    sum_xy = np.sum(x * y)

    # Calcular el denominador y verificar que no sea 0
    denominador = (n * sum_xx - sum_x ** 2)
    if denominador == 0:
        raise ValueError("No se puede calcular la regresión porque todos los valores de x son iguales.")

    # Calcular coeficientes de la recta
    a = (n * sum_xy - sum_x * sum_y) / denominador
    b = (sum_y - a * sum_x) / n

    return {"a": a, "b": b, "equation": f"y = {a:.4f}x + {b:.4f}"}