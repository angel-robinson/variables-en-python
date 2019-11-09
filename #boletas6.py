#input
cliente=input("ingrese el nombre de cliente:")
precio_producto=float(input("ingrese el precio del producto:"))
descuento_producto=float(input("ingrese el descueno del producto:"))
cantidad_productos=int(input("ingrese la cantidad de productos:"))
#procesing
ganancia=cantidad_productos*(precio_producto-descuento_producto)
#vereficador
ganacia_regular=(ganancia>=50)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# EL NOMBRE DEL CLIENTE ES        :",cliente)
print("# EL PRECIO DE CADA PRODUCTO ES   :",precio_producto)
print("# EL DESCUENTO DE CADA PRODUCTO ES:",descuento_producto)
print("# GANANCIA TOTAL                  :",ganancia)
print("###############################")
print("¿HAY UNA GANANCIA REGULAR?:",ganacia_regular)

