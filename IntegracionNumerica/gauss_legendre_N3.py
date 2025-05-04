import numpy as np
from scipy.special import roots_legendre

def cuadratura_Gauss_Legendre_N3(fx, inf, sup):

    # Obtener nodos y pesos para N=3
    nodos, pesos = roots_legendre(3)

    # Transformar los nodos al intervalo [inf, sup]
    x_transformados = 0.5 * (sup - inf) * nodos + 0.5 * (sup + inf)

    # Evaluar la función en los nodos
    try:
        valores_fx = fx(x_transformados)
    except Exception as e:
        return {"error": f"Error al evaluar la función: {e}"}

    # Calcular la integral
    integral = 0.5 * (sup - inf) * np.sum(pesos * valores_fx)

    return {"integral": integral}