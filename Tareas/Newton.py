# https://perhuaman.files.wordpress.com/2014/06/metodos-numericos-wmora.pdf
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.lagrange.html
import math as mt
import numpy as np
import sympy as sp
from scipy.interpolate import lagrange


def newton(rX, rY):
    polinomio = rY[0]
    tablaDiff = np.concatenate(([rX], [rY]), axis=0)  # quedan como filas
    tablaDiff = np.transpose(tablaDiff)  # invierto y quedan como columnas
    diffNewton = np.zeros((len(rX), len(rX)), dtype=float)
    tablaDiff = np.concatenate((tablaDiff, diffNewton), axis=1)
    diagonal = len(rX) - 1

    for j in range(2, len(rX) + 2):
        numerador = 1
        denominador = 1
        for i in range(0, diagonal):
            numerador = tablaDiff[i + 1][j - 1] - tablaDiff[i][
                j - 1]  # resto de la columna anterior la fila siguiente - en la que estoy
            denominador = tablaDiff[i + (j - 1)][0] - tablaDiff[i][0]
            tablaDiff[i][j] = numerador / denominador
        diagonal -= 1
    f = sp.Symbol('x')
    coefNewton = tablaDiff[0, 2:]
    tamNewton = len(coefNewton)
    for j in range(1, tamNewton):
        newton = coefNewton[j - 1]
        resto = 1
        for i in range(0, j):
            resto = resto * (f - rX[i])
        polinomio = polinomio + resto * newton
    print(polinomio)
    print("-----------------------------------------------------------------------------")
    return polinomio


# DATOS
x0 = 0
x1 = 1
x2 = 2

y0 = 10.5
y1 = 15.33
y2 = 5.789

arregloX=np.array([x0, x1,x2])
arregloY=np.array([y0, y1,y2])

x = sp.Symbol('x')
print("Newton")
polinomioN = newton(arregloX, arregloY)
print("Newton simplificado")
polinomioN = polinomioN.expand()
print(polinomioN)
print("-----------------------------------------------------------------------------")
print("Lagrange")
polinomioL = lagrange(arregloX, arregloY)
print(polinomioL)

