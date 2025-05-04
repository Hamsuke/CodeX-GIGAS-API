import sympy as sp


def newton_polinomios(expr_str, valor_inicial):
    x_sym = sp.Symbol('x')

    # Crear la función y su derivada
    funcion = sp.sympify(expr_str)
    derivada = sp.diff(funcion, x_sym)

    # Funciones evaluables
    def funcion_evaluar(x):
        return funcion.subs(x_sym, x).evalf()

    def funcion_derivada(x):
        return derivada.subs(x_sym, x).evalf()

    # Método de Newton
    x = valor_inicial
    tol = 1e-6
    max_iter = 50

    for i in range(max_iter):
        fx_val = funcion_evaluar(x)
        dfx_val = funcion_derivada(x)

        if abs(fx_val) < tol:
            return {
                "raiz": float(x),
                "iteraciones": i + 1
            }

        if dfx_val == 0:
            raise ValueError("La derivada se anuló, no se puede continuar con el método de Newton")

        x_next = x - fx_val / dfx_val

        if abs(x_next - x) < tol:
            return {
                "raiz": float(x_next),
                "iteraciones": i + 1
            }

        x = x_next

    raise ValueError("El método no convergió en el número máximo de iteraciones")