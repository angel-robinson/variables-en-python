#encontrar la acceleracion centripeta
#input
velocidad_tangencial=float(input("ingrese la velocidad tangencial:"))
radio=float(input("ingrese el radio:"))
#procesing
acceleracion_centripeta=(velocidad_tangencial/radio)
#vereficador
acceleracion_centripeta_regular=(acceleracion_centripeta>20)
#output
print("la acceleracion centripeta es:")
print("¿la acceleracxion centripet es la adecuada?",acceleracion_centripeta_regular)
