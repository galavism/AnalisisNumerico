import math
import sympy

def main():

    a=  int(input("Digite lim inferior"))
    b= int (input("Digite lim superior"))
    tol = int(input("Digite la tolerancia"))

    x=sympy.Symbol("x")
    funcion = x*math.e**x-math.pi #DEFINO LA FUNCIÓN L math.cos(x)-x
    condicion=abs(b-a)
    cont = 0

    if (funcion.subs(x,a)*funcion.subs(x,b)>0):
        print("La funcion no tiene ceros en este intervalo")

    else:
      while(condicion>10**tol):
         cont+=1
         c=(a+b)/2
         if (funcion.subs(x,c)*funcion.subs(x,a)<0):
             b=c
         if(funcion.subs(x,c)*funcion.subs(x,a)>0):
             a=c
         if(funcion.subs(x,c)*funcion.subs(x,a)==0):
             print("La raiz es: {}".format(c))
             break

         print("La iteracion es  {} aproximacion a la raiz {}".format(cont, c))
         condicion=abs(b-a)

main()