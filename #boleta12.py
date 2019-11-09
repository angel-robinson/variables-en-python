#input
cliente=input("ingrese el nombre del cliente:")
auriculares=int(input("ingrese la cantidad de auriculares:"))
usb=int(input("ingrese la cantidad de usb:"))
precio_auricular=float(input("ingrese el precio de cada auricular:"))
precio_usb=float(input("ingrese el precio de cada usb:"))
#procesing
pago_total=precio_auricular*auriculares+precio_usb*usb
#vereficador
cliente_bueno=(pago_total>50)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# el cliente es        :",cliente)
print("# numero auriculares es:",auriculares," precio:",precio_auricular)
print("# numero de usb        :",usb,"         precio:",precio_usb)
print("# pago total           :",pago_total)
print("###############################")
print("¿el cliente invertio ?:",cliente_bueno)
