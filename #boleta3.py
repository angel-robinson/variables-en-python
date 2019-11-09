#input
producto=(input("ingrese el producto:"))
costo=float(input("ingrese el costo del producto:"))
rebaja=float(input("ingresa el descuento:"))
#procesing
costo_total=(costo-rebaja)
#vereficador
producto_calidad=(costo_total>=250)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("#NOMBRE DEL PRODUCTO :",producto)
print("# PRECIO PRODUCTO    :",costo)
print("costo total s/.      :",costo_total)
print("###############################")
print("¿el producto es de alta calidad?:",producto_calidad)

