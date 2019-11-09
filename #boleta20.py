#input
cliente=input("ingrese el nombre del cliente:")
muebles=float(input("ingrese la cantidad de muebles:"))
precio_muebles=float(input("ingrese el precio:"))
#procesing
pago_total=muebles*precio_muebles
#vereficador
inversion_muebles=(pago_total>=2000)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# el cliente es            :",cliente)
print("# numero total de muebles  :",muebles)
print("# precio de cada mueble es :s/.",precio_muebles)
print("# pago total               :",pago_total)
print("###############################")
print("¿el cliente invirti mas de s/.2000 ?:",inversion_muebles)
