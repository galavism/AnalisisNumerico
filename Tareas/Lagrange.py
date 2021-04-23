#con la funcion f(x)=Inx contruya la interpolación en x0=1
#x1=2 y estime el error en [1,2]

import math as mt
import numpy as np
import sympy as sp
from scipy.interpolate import lagrange

#DATOS

x0=1
x1=2
y0=mt.log(x0)
y1=mt.log(x1)

#arregloX=np.array([x0, x1])
#arregloY=np.array([y0, y1])

#arregloX=np.array([6,8,10,12,14,16,18])
#arregloY=np.array([7,9,12,18,21,19,15])

arregloX = np.array([40, 50, 60, 70, 80])
arregloY = np.array([35,83,153,193,215])

#FORMULA LAGRANGE

#SUMATORIA DE LA PRODUCTORIA Li(X)* Yi
polinomio=0
tam=len(arregloX)
x=sp.Symbol('x') #para el polinomio

for i in range (0,tam):
    numerador=1
    denominador=1
    for j in range (0,tam):
        if j!=i:
            numerador=numerador*(x-arregloX[j])
            denominador=denominador*(arregloX[i]-arregloX[j])
    Li=numerador/denominador*arregloY[i]
    polinomio=polinomio+(Li)



#print("Polinomio Lagrange es {}".format(polinomio))
print("---------------------------------------------------------------------------")
#print("Polinomio Lagrange simplificado {}".format(polinomio.expand()))
polinomioL=lagrange(arregloX,arregloY)
print("---------------------------------------------------------------------------")
print ("Ahora con la librería: {}".format(polinomioL))
print("---------------------------------------------------------------------------")
print(polinomio.subs(x,55))
#print("Diferencia con wolfram: {}".format(-polinomio.subs(x,6.5)+8.0598808078125))








