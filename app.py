from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Union

#Import para los metodos matematicos proporcionados por jorge}
from InterpolacionPolinomial.minimos_cuadrados import minimos_cuadrados
from IntegracionNumerica.gauss_legendre_N3 import cuadratura_Gauss_Legendre_N3

app = FastAPI()

class DataPoints(BaseModel):
    Method: int
    X: Union[str] = None
    Y: Union[str] = None
    FX: Optional[str] = None
    H: Optional[float] = None
    N: Optional[int] = None
    VALI: Optional[float] = None

@app.post("/app/procesar")
def read_root(data: DataPoints):
    data : DataPoints
    seleccion = int(data.Method)
    match seleccion:
        case 1:
            return {"metodo" : "Biseccion"}
        case 2:
            return {"Regla falsa"}
        case 3:
            return {"Secante"}
        case 4:
            return {"Newton - Raphson"}
        case 5:
            return {"Punto fijo"}
        case 6:
            return {"Newton - Raphson aplicado a sistemas no lineales"}
        case 7:
            return {"Punto fijo aplicado a sistemas no lineales"}
        case 8:
            return {"Bairstow"}
        case 9:
            #return {"Newton"}
            try:
                result = newton_polinomios(expr_str, valor_inicial)
                return {"resultado": result}
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))
        case 10:
            return {"Vandermonde"}
        case 11:
            return {"Interpolacion de newton"}
        case 12:
            return {"Interpolacion Baricentrica (Lagrange)"}
        case 13:
            #return {"Minimos Cuadrados"}
            try:
                result = minimos_cuadrados(data.X, data.Y)
                return {"resultado": result}
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))
        case 14:
            return {"Polinomios ortogonales de Chebyshev"}
        case 15:
            return {"Formula cerrada de Newton - Cotes  N = 1"}
        case 16:
            return {"Formula cerrada de Newton - Cotes N = 2"}
        case 17:
            #return {"Formula cerrada de Newton - Cotes N = 3"}
            try:
                result = cuadratura_Gauss_Legendre_N3(fx, inf, sup)
                return {"resultado": result}
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))
        case 18:
            return {"Formula abierta de Newton - Cotes N = 0"}
        case 19:
            return {"Formula abierta de Newton - Cotes N = 1"}
        case 20:
            return {"Formula abierta de Newton - Cotes N = 2"}
        case 21:
            return {"Formula de integracion de Romberg"}
        case 22:
            return {"Cuadraturas de Gauss - Legendre N = 2"}
        case 23:
            #{"Cuadraturas de Gauss - Legendre N = 3"}
            #data.H y data.VALI representan limite inferior y superior respectivamente
            try:
                result = cuadratura_Gauss_Legendre_N3(data.FX,data.H, data.VALI)
                return {"resultado": result}
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))
        case 24:
            return {"Euler"}
        case 25:
            return {"Euler - Cauchy (Regla Tapezoidal)"}
        case 26:
            return {"Runge - Kuta (Euler Modificado"}
        case 27:
            return {"Runge - Kuta [Orden 2]"}
        case 28:
            return {"Metodo Predictor - Corrector"}
        case 29:
            return {"Euler"}
        case 30:
            return {"Euler - Cauchy (Regla Tapezoidal)"}
        case 31:
            return {"Runge - Kuta (Euler Modificado"}
        case 32:
            #return {"Runge - Kuta [Orden 2]"}
            try:
                result = runge_kutta_orden2_func(f_str, x0, y0, h, n):
                return {"resultado": result}
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))