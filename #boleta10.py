##input
cliente=input("regriste le nombre del cliente:")
zapatillas=int(input("pares de zapatillas:"))
costo_zapatillas=float(input("ingrese el costo de la zapatilla:"))
tamaño=int(input("ingrese el talla de la zapatilla:"))
#procesing
total=(costo_zapatillas*zapatillas)
#vereficador
cliente_favorable=(total>200)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# EL CLIENTE ES       :",cliente)
print("#NUMERO DE ZAPATILLAS :",zapatillas)
print("#COSTO DE LA ZAPATILLA:",costo_zapatillas)
print("# EL TAMAÑO DE LA ZAPATILLA ES:",tamaño)
print("# GANANCIA TOTAL:",total)
print("###############################")
print("¿CONVIENE QUE EL COMPRADOR SEA CLIENTE?:",cliente_favorable)
