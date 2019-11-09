#input
pasajero=input("ingrese el nombre de pasajero:")
numero_de_pasajes=int(input("ingrese la cantidad de pasajes:"))
precio_pasaje=float(input("precio del pasaje:"))
#procesimg
costo_pasajero=(numero_de_pasajes*precio_pasaje)
#vereficador
costo_excesivo=(costo_pasajero>=50)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("#PASAJERO          :",pasajero)
print("# PRECIO DEL PASAJE:",precio_pasaje)
print("COSTO POR PASJERO  :",costo_pasajero)
print("###############################")
print("¿EL COSTO ES EXCESIVO?:",costo_excesivo)
