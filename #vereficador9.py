#encontrar la masa de un cuerpo
#input
fuerza=float(input("ingrese la fuerza:"))
acceleracion=float(input("ingrese la acceleracion:"))
#procesing
masa=fuerza/acceleracion
#vereficador
masa_adecuada=(masa>=20)
#output
print("la masa del cuerpo es:",masa)
print("la masa es adecuada?",masa_adecuada)
