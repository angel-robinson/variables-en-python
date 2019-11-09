#input
cliente=input("ingrese el nombre del cliente:")
gorras=int(input("ingrese la cantidad de gorras:"))
precio_gorras=float(input("ingrese el precio de cada gorra:"))
polos=int(input("ingrese la cantidad de poloss:"))
precio_polos=float(input("ingrese el precio de cada polo:"))
#procesing
pago_total=precio_gorras*gorras+precio_polos*polos
#vereficador
cliente_procutos=(polos+gorras>5)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# el cliente es     :",cliente)
print("# numero gorras es  :",gorras," precio:s/.",precio_gorras)
print("# numero de polos es:",polos," precio:s/.",precio_polos)
print("# pago total        :",pago_total)
print("###############################")
print("¿llevo mas que cinco productos?:",cliente_procutos)
