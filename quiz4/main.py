pregunta = input("Ingrese lo que desee: ")
cadena=""
lista=[]
frase=""
cont=0
contx=0

while cadena!="salir":
    cadena = input("Ingrese lo que desee: ")
    if "agua" in cadena:
        cont=cont+1
        lista.append(cadena)
    if "fuego" in cadena:
        contx = contx+1
        lista.append(cadena)
print("Agua= ", cont)
print("Fuego= ", contx)
print(lista)






