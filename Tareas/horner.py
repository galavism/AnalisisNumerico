#ESTA FUNCIÓN RECIBE EL POLINOMIO QUE SE VA A RESOLVER Y CUYA CANTIDAD DE MULTIPLICACIONES SE QUIERE CONOCER
def evalPoli(polinomio, x):

  suma = multi = 0
  r = polinomio[0]
  n = len(polinomio)

  for i in range (1, n):
      r = polinomio[i] + r * x
      multi = multi + 1
      suma = suma + 1

  print ("El resultado  del polinomio es: {} con un total de sumas: {} y un total de multplicaciones:  {}".format(r,suma,multi))


#DEFINICION DEL MAIN PROGRAMA PRINCIPAL
def main ():


 repetir=True

 print("Bienvenido al programa que resuelve un polinomio con el método de Horner\n")

 while(repetir==True):
     polinomio = []
     gradoP=int(input("¿Cuál es el grado del polinomio?\n"))

     aux=gradoP

     print("Recuerde ORDENAR el polinomio en forma DESCENDENTE")

     for i in range (0,(gradoP+1)):
             num=int(input("\nIngrese el coeficiente del x^{}\n".format(aux)))
             polinomio.append(num)
             aux = aux - 1

     x=int(input("Ingrese el valor de X para el polinomio: "))

     evalPoli(polinomio,x)

     rta=input("Desea evaluar otro polinomio? s(si)/n(no)")
     rta=rta.lower()

     if (rta=='n'):
      repetir=False

#LLAMADO A LA FUNCIÓN MAIN
main()






