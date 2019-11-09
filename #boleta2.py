#input
nombre=input("ingrese el nombre del cliente:")
producto_comprado=int(input("ingrese la cantidad de productos comprados:"))
precio=float(input("ingrese el precio del producto:"))

#procesing
precio_total=(producto_comprado*precio)
#verificador
precio_total_barato=(precio_total<=20)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# cliente           :",nombre)
print("#NOMBRE DEL PRODUCTO:",producto_comprado)
print("# PRECIO PRODUCTO   :",precio)
print("costo total s/.     :",precio_total)
print("###############################")
print("producto barato     :",precio_total_barato)
