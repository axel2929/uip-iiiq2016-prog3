def capturar():
    b = True
    while b:
        q = int(input("QUIZ: "))
        if (q < 0) or (q > 100):
            print("Intente nuevamente.")
        else:
            b = False
    while b == False:
        p = int(input("PARCIAL: "))
        if (p < 0) or (p > 100):
            print("Intente nuevamente.")
        else:
            b = True
    while b == True:
        e = int(input("EXAMEN: "))
        if (e < 0) or (e > 100):
            print("Intente nuevamente")
        else:
            break
    return q,p,e

def calcular(q, p, e):
    if q == -1:
        print("Por favor ingrese las notas")
    else:
        prom = (q + p + e) / 3.0
        print("Tu promedio es " + str(prom))

def menu():
    print("MENU\n1. Ingresar notas\n2. Calcular promedio\n3. Salir")


if __name__ == '__main__':
    q = -1
    p = -1
    e = -1
    opcion = 0

    while opcion != 3:
        menu()
        opcion = int(input("Opcion: "))

        if opcion == 1:
            q, p, e = capturar()
        elif opcion == 2:
            calcular(q, p, e)
        elif opcion == 3:
            pass
        else:
            print("Opcion no valida!")
