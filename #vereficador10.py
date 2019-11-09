#encontrar la velocidad media
#input
velocidad1=float(input("ingrese la primera velocidad:"))
velocidad2=float(input("ingrese la segunda velocidad:"))
distancia=float(input("ingrese la distancia:"))
#procesing
velocidad_media=(velocidad1+velocidad2)/distancia
#vereficador
velocidad_media_regular=(velocidad_media>=40)
#output
print("la velocidad media es:",velocidad_media)
print("¿velocidad media regular es adecuada?",velocidad_media_regular)
