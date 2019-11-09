#input
nombre=input("ingrese el nombre:")
producto1=input("ingrese el primer producto:")
costo1=float(input("costo primer producto:"))
producto2=input("ingrese el segundo producto:")
costo2=float(input("costo segundo producto:"))
#procesing
costo_total_productos=(costo1+costo2)
#verificador
costo_total_productos_pago=(costo_total_productos<20)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# cliente         :",nombre)
print("# primer producto :",producto1,"  COSTO:",costo1)
print("# segundo producto:",producto2,"  COSTO:",costo2)
print("costo total s/.   :",costo_total_productos)
print("###############################")
print("los productos son de facil pago:",costo_total_productos_pago)
