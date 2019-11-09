#vereficador1
#input
distancia=float(input("ingrese la distancia:"))
tiempo=float(input("ingrese el tiempo:"))
#procesing
velocidad=(distancia/tiempo)
#vereficador
velocidad_adecuada=(velocidad>12)
#output
print("el valor de la velocidad es:",velocidad)
print("¿el moviltiene una veocidad adecuada?",velocidad_adecuada)
