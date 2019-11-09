#emcontrar la energia elastica
#input
const_elastica=float(input("ingrese la constante elastica:"))
deformacion=float(input("ingrese la deformacion de cuerpo:"))
#procesing
energia_elastica=(const_elastica*deformacion**2)/2
#vereficador
energia=(energia_elastica>=1)
#output
print("la energia elastica es:",energia_elastica)
print("¿la energia elastica del cuerpo es positivo?",energia)
