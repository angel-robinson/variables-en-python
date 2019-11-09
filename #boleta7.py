#input
numero_cliente=int(input("ingrese el numero de clientes:"))
producto1=float(input("ingrese el precio del producto:"))
producto2=float(input("ingrese el precio del producto:"))
#procesing
ganancia=(producto1+producto2)*numero_cliente
#vereficador
ganancia_adecuada=(ganancia>4)
# OUTPUT
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# EL NUMERO DE CLIENTES ES        :",numero_cliente)
print("# EL PRECIO DEL PRIMER PRODUCTO ES:",producto1)
print("# PRECIO DEL SEGUNDO PRODUCTO ES  :",producto2)
print("# GANANCIA TOTAL                  :",ganancia)
print("###############################")
print("¿HAY UNA GANANCIA ADECUADA?:",ganancia_adecuada)
