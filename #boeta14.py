#input
cliente=input("ingrese el nombre del cliente:")
sandalias=int(input("ingrese la cantidad de sandalias:"))
precio_sandalias=float(input("ingrese el precio de cada auricular:"))
shorts=int(input("ingrese la cantidad de shorts:"))
precio_shorts=float(input("ingrese el precio de cada usb:"))
#procesing
pago_total=precio_sandalias*sandalias+precio_shorts*shorts
#vereficador
cliente_procutos=(sandalias+shorts>5)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# el cliente es    :",cliente)
print("# numero sandalias es:",sandalias," precio:s/.",precio_sandalias)
print("# numero de short es:",shorts," precio:s/.",precio_shorts)
print("# pago total   :",pago_total)
print("###############################")
print("¿llevo mas que cinco productos?:",cliente_procutos)
