import math

def punto_fijo(g, valor_inicial):
    tolerancia = 1e-6
    max_iter = 50
    x = valor_inicial
    for i in range(max_iter):
        # Calculamos el siguiente valor de x
        x_next = g(x) 
        # Verificamos si la diferencia entre iteraciones es menor que la tolerancia
        if abs(x_next - x) < tolerancia:
            # Si se cumple, retornamos la raíz aproximada y el número de iteraciones
            return x_next, i+1
        # Actualizamos x para la siguiente iteración
        x = x_next
    raise ValueError("El método no convergió en el número máximo de iteraciones")

def evaluar_fx(x):
    # Incluir todas las funciones matemáticas disponibles
    contexto = {func: getattr(math, func) for func in dir(math) if callable(getattr(math, func))}
    contexto["x"] = x
    return eval(funcion_entrada, contexto)

funcion_entrada = input("Ingrese la función iterativa: ")
valor_inicial = float(input("Ingrese el valor inicial: "))

raiz, iteraciones = punto_fijo(evaluar_fx, valor_inicial)
print("Aproximación de la raíz:", raiz)
print("Iteraciones realizadas:", iteraciones)