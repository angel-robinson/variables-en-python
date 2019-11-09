#encontrar la enegia potencial gravitatoria
#input
masa=float(input("ingrese la masa:"))
gravedad=float(input("ingrese la gravedad:"))
altura=float(input("ingrese la altura:"))
#procesing
energia_gravitatoria=(masa*altura*gravedad)
#vereficador
energia_gravitatoria_adecuada=(energia_gravitatoria>100)
#output
print("la energia potenciala gravitatoria es:",energia_gravitatoria)
print("¿la energia potencial graviatoria es la adecuada?",energia_gravitatoria_adecuada)
