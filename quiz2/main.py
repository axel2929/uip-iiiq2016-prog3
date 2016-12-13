pregunta = input("Ingrese lo que desee: ")
x=""
y=""
letra=None

indice = 0
while indice < len(pregunta):
    letra = pregunta[indice]
    if letra == "¿":
        x=letra
    elif letra == "?":
        y=letra
    indice += 1
    if x!="" and y!="":
        print("Ofi")
    else:
        if pregunta="":








