# Conversor de monedas

print("Conversor de centavos a Billetes")

centavos = float(input("Ingresa cantidad de centavos: "))

dolares=centavos/100
euros=dolares*0.8965
yen=dolares*101.5744
bp=dolares*0.7702
mxn=dolares*19.7843

print("Centavos: " + str(centavos))
print("Dolares: " + str(dolares))
print("EUR: " + str(euros))
print("YEN: " + str(yen))
print("BP: " + str(bp))
print("MXN: " + str(mxn))


