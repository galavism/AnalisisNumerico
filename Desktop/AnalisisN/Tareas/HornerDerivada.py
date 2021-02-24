# ESTA FUNCIÓN RECIBE EL POLINOMIO QUE SE VA A RESOLVER Y CUYA CANTIDAD DE MULTIPLICACIONES SE QUIERE CONOCER

def evalPoli(polinomio, x, gradoP):
    suma = multi = 0
    r = polinomio[0]
    n = len(polinomio)

    # gradoP es el grado del polinomio-1 para el cálculo de la derivada. POR EJEMPLO: gradP=4, graP=3
    gradoP = gradoP - 1
    # deriv es el primer coeficiente POR el valor de x ELEVADO al exponente de la derivada. POR EJEMPLO: 2*(1)^3
    deriv = r * (x ** gradoP)

    for i in range(1, n):

        r = polinomio[i] + r * x
        multi = multi + 1
        suma = suma + 1

        if i < (n - 1):
            gradoP = gradoP - 1
            deriv = deriv + r * (x ** gradoP)
            print("PARA TENER EN CUENTA  r ES : {} Y deriv es {}".format(r, deriv))

    print("El resultado  del polinomio es: {} con un total de sumas: {} y un total de multplicaciones:  {}".format(r,
                                                                                                                   suma,
                                                                                                                   multi))
    print("LA DERIVADA ES {}".format(deriv))


# DEFINICION DEL MAIN PROGRAMA PRINCIPAL

def main():
    repetir = True
    print("Bienvenido al programa que resuelve un polinomio con el método de Horner\n")
    while (repetir == True):
        polinomio = []
        gradoP = int(input("¿Cuál es el grado del polinomio?\n"))

        aux = gradoP

        print("Recuerde ORDENAR el polinomio en forma DESCENDENTE")

        for i in range(0, (gradoP + 1)):
            num = int(input("\nIngrese el coeficiente del x^{}\n".format(aux)))
            polinomio.append(num)
            aux = aux - 1

        x = int(input("Ingrese el valor de X para el polinomio: "))

        evalPoli(polinomio, x, gradoP)

        rta = input("Desea evaluar otro polinomio? s(si)/n(no)")
        rta = rta.lower()

        if (rta == 'n'):
            repetir = False


# LLAMADO A LA FUNCIÓN MAIN
main()
