#encontrar la acceleracion del cuerpo
#input
veloc_final=float(input("ingrese la velocidad final:"))
veloc_inicial=float(input("ingrese la velocidad inicial"))
tiempo=float(input("ingrese el tiempo:"))
#procesing
acceleracion=(veloc_final-veloc_inicial)/tiempo
#vereficador
acceleracion_desacceleracion=(acceleracion>0)
#output
print("la accceleracion del movil es:",acceleracion)
print("¿el movil accelera?",acceleracion_desacceleracion)
