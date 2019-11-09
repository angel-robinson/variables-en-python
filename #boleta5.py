#input
clientes=int(input("ingrese la cantidad de clientes:"))
compras_por_dia=int(input("ingrese la cantidad de compras por cliente"))

#procesing
efectivo=(clientes*compras_por_dia)
#vereficador
clientes_regulares=(clientes>=20)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# EL NUMERO DE CLIENTES ES       :",clientes)
print("# COMPRAS AL DIA POR CADA CLIENTE:",compras_por_dia)
print("# EL EFECTIVO QUE SE OBTUVO ES   :",efectivo)
print("###############################")
print("¿HAY CLIENTES REGULARES?:",clientes_regulares)

