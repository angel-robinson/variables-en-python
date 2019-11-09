#input
cliente=input("ingrese el nombre del cliente:")
parlantes_numero=float(input("ingrese la cantidad de los parlantes:"))
precio_parlantes=float(input("ingrese el precio:"))
#procesing
pago_total=precio_parlantes*parlantes_numero
#vereficador
buena_venta=(pago_total>=100)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# el cliente es            :",cliente)
print("# numero total de parlantes:",parlantes_numero)
print("# precio de cada celular es:s/.",precio_parlantes)
print("# pago total               :",pago_total)
print("###############################")
print("¿se hizo una buena venta ?:",buena_venta)
