# MI PRIMER PROGRAMA
'''
print("Phyton es un lenguaje interpretado.")

print("Bienvenido a la calculadora de ITBMS")

ITBMS = 0.07
subtotal= float(input("Subtotal: "))
total = subtotal * ITBMS

print("El impuesto de " + str(subtotal) + " es " + str(total))
'''
print("Identificador de adultos")

nombre= input("Dame tu nombre: ")
edad = input("Dame tu edad: ")

if int(edad) >= 8:
    print("Eres adulto, " + nombre)
else:
    print("Eres menor, lapecillo")

