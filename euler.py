"""
    euler.euler.py
    Lisandro M. Toledo
    Legajo: 9125
    Ingeniería en Sistemas
"""

import math

# Cálculo de x para cada paso.
def x_sub_n(a, n, delta_x):
    return a + n*delta_x

# Determinar la cantidad de pasos.
def contar_pasos(x1, x2, paso):
    return int((x2 - x1) / paso)

# y = y_sub(n - 1) + delta_x* f(x_sub(n-1), y_sub(n-1))
def euler(x_inicial, x_final, delta_x, y_inicial, f):
    x = x_inicial
    y = y_inicial
    pasos = contar_pasos(x_inicial, x_final, delta_x)

    for i in range(pasos):
        x = x_sub_n(x_inicial, i, delta_x)
        y = y + delta_x*f(x, y)
    
    return y

# Convertir una cadena en una función.
def traducir_func(cadena_func):
    while True:
        try:
            f = eval("lambda x, y: " + cadena_func.replace('^', '**').replace('sqrt', 'math.sqrt').replace('e', 'math.e'))
            break
        except Exception as e:    
            print("ERROR:", e)
            exit()
    return f


if __name__ == "__main__":
    # Ejercicio 1
    print("============================================================================================")
    print("Ejercicio 1\nConsidera el problema con valor inicial dy/dx = 0.2xy con y(1) = 1. Usa el programita para\n"
    "aproximar y(1.5) usando primero un paso de 0.1 y luego de 0.05.")
    print("---------------------------------------------------------------------------------------------")

    print("Ecuación diferencial: dy/dx = 0.2xy")
    print("Condiciones iniciales: y(1) = 1")

    #Cargando función
    edo = "0.2*x*y"

    #Convirtiendo función a código
    f = traducir_func(edo)

    #Estableciendo condiciones iniciales
    x_inicial = 1
    y_inicial = 1

    #Valor a aproximar
    x_final = 1.5

    print(f"Valor a aproximar: y({x_final})")

    #Tamaño del paso (delta x)
    paso = [0.1, 0.05]

    for p in paso:
        r = euler(x_inicial, x_final, p, y_inicial, f)
        print(f"Con paso {p}: {r}")


    print("\n\n============================================================================================")
    print("Ejercicio 2\nConsidera un circuito simple donde la resistencia es 12 Ω, la inductancia es 4 H y la batería\n"
    "da un voltaje constante de 60 V. Si el interruptor está cerrado cuando t = 0, se modela la\n"
    "corriente I en el tiempo t mediante el problema con valores iniciales dI/dt = 15 − 3I, I(0) = 0.\n"
    "Estima la corriente en el circuito medio segundo después de que se cierra el interruptor.")
    print("---------------------------------------------------------------------------------------------")

    print("Ecuación diferencial: dI/dt = 15 − 3I")
    print("Condiciones iniciales: I(0) = 0")

    # Cargando función
    edo = "15-3*y"

    # Convirtiendo función a código
    f = traducir_func(edo)

    # Estableciendo condiciones iniciales
    x_inicial = 0
    y_inicial = 0

    # Valor a aproximar
    x_final = 0.5 #(medio segundo después)
    print(f"Valor a aproximar: y({x_final})")

    #Tamaño del paso arbitrario
    paso = 0.005 # 0.5/100 

    r = euler(x_inicial, x_final, paso, y_inicial, f)
    print(f"Con paso {paso}: {r}")
    