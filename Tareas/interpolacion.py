
import math as mt
import numpy as np
import sympy as sp
from scipy.interpolate import CubicSpline
from scipy.interpolate import lagrange

x=sp.Symbol('x')

def lagrange (arregloX, arregloY):
    # FORMULA LAGRANGE
    polinomio = 0  # acá se van a acumular todos los términos
    tam = len(arregloX)  # cantidad de puntos
    productoria = 1

    for i in range(0, tam):
        numerador = 1
        denominador = 1
        for j in range(0, tam):  # termino por termino
            if j != i:  # en la productoria j != i
                numerador = numerador * (x - arregloX[j])  # (x-arregloX [pos diferente en la que estoy en i])
                denominador = denominador * (arregloX[i] - arregloX[j])  # (arregloX[pos i]-arregloX [pos diferente en la que estoy en i])
        Li = numerador / denominador * arregloY[i]  # el termino del polinomio esta compuesto por Y[i]*la división de los términos anteriormente calculados
        polinomio = polinomio + (Li)  # sumatoria de todos los términos
        productoria = productoria * (x - arregloX[i])
    return polinomio


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
    return polinomio

def errorLineal (M,x1,x0):
    # fórmula error interpolación lineal general
    # |f(x)-p1(x)|=M*(x1-x0)^2/8
    # M max absoluto
    pError = M * abs(((x1 - x0) ** 2) / 8)
    print("El error general lineal es:  {}".format(pError))

def errorGenCuad(M,x1,x0):
    # fórmula error interpolación cuadrática
    # |f(x)-p2(x)|=M*h^3/9(3)^(1/2)
    # M max absoluto
    # h es el valor del espacio constante
    h = x1-x0
    pError = (M* h ** 3) / (9 * (3) ** (1 / 2))
    print("El error general cuadrático es:  {}".format(pError))

def errorGenCub(M,x1,x0):
    # fórmula error interpolación cubica
    # |f(x)-p2(x)|=M*h^4/24
    # M max absoluto
    # h es el valor del espacio constante
    h = x1 - x0
    pError = M * h ** 4 / 24
    print("El error general cúbico es:  {}".format(pError))

print("Escoja la opcion que desea")

print("1.Logaritmo")
print("2.Error general cuadrática seno")
print("3.Error general cúbica seno")
print("4.Temp")

opc=int(input("Opción: "))
if (opc==1):
    # DATOS
    x0 = 1
    x1 = 2
    y0 = mt.log(x0)
    y1 = mt.log(x1)

    arregloX = np.array([x0, x1])
    arregloY = np.array([y0, y1])

    # LLAMADO
    polinomioN = newton(arregloX, arregloY)
    print("Newton:  {}".format(polinomioN))
    print("-----------------------------------------------------------------------------")
    polinomioL = lagrange(arregloX, arregloY)
    print("Lagrange: {}".format(polinomioL.simplify()))
    print("-----------------------------------------------------------------------------")
    errorLineal(13.85,arregloX[1],arregloX[0]) #13.85 sale de calcular el máximo en wolfram

if (opc==2):
    # DATOS
    x0 = 0
    x1 = 0.01
    x2 = 0.02

    y0 = mt.sin(x0)
    y1 = mt.sin(x1)
    y2 = mt.sin(x2)

    arregloX = np.array([x0, x1, x2])
    arregloY = np.array([y0, y1, y2])

    # LLAMADO
    polinomioN = newton(arregloX, arregloY)
    print("Newton:  {}".format(polinomioN))
    print("-----------------------------------------------------------------------------")
    polinomioL = lagrange(arregloX, arregloY)
    print("Lagrange: {}".format(polinomioL.simplify()))
    print("-----------------------------------------------------------------------------")
    errorGenCuad(1,arregloX[1],arregloX[0])

if (opc==3):
    # DATOS
    # DATOS
    x0 = 0
    x1 = 0.01
    x2 = 0.02
    x3 = 0.03

    y0 = mt.sin(x0)
    y1 = mt.sin(x1)
    y2 = mt.sin(x2)
    y3 = mt.sin(x3)

    arregloX = np.array([x0, x1, x2,x3])
    arregloY = np.array([y0, y1, y2,y3])

    # LLAMADO
    polinomioN = newton(arregloX, arregloY)
    print("Newton:  {}".format(polinomioN))
    print("-----------------------------------------------------------------------------")
    polinomioL = lagrange(arregloX, arregloY)
    print("Lagrange: {}".format(polinomioL.simplify()))
    print("-----------------------------------------------------------------------------")
    errorLineal(1,arregloX[1],arregloX[0])

if (opc==4):
    # DATOS

    arregloX=np.array([6,8,10,12,14,16,18,20])
    arregloY=np.array([7,9,12,18,21,19,15,10])

    # LLAMADO
    polinomioN = newton(arregloX, arregloY)
    print("Newton:  {}".format(polinomioN))
    print("-----------------------------------------------------------------------------")
    polinomioL = lagrange(arregloX, arregloY)
    print("Lagrange: {}".format(polinomioL.simplify()))
    print("-----------------------------------------------------------------------------")
    cs = CubicSpline(arregloX, arregloY)
    print("-----------------------------------------------------------------------------")

    ult=arregloX[len(arregloX)- 1]
    hora=arregloX[0]
    print (ult)
    while(hora<20.5):
        print("Los grados con Lagrange en {} es {}".format(hora,polinomioL.subs(x,hora)))
        print("Los grados con Newton en {} es {}".format(hora, polinomioN.subs(x, hora)))
        print("Los grados con Spline Cubic en {} es {}".format(hora, cs(hora)))
        hora+=0.5