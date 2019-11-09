#input
cliente=(input("ingrese le nombre del cliente :"))
kg_arroz=int(input("ingrese el numero de kg de arroz :"))
costo_arroz=float(input("ingrese el precio del arroz :"))
kg_papa=int(input("ingrese el numero de kg de papa :"))
costo_papa=float(input("ingrese el precio de la papa:"))
#procesing
total=(kg_arroz*costo_arroz)+(kg_papa*costo_papa)
#vereficador
comprador_compulsivo=(total>100)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# EL CLIENTE ES    :",cliente)
print("# Nr DE KG DE ARROZ:",kg_arroz," COSTO DEL ARROZ   :",costo_arroz)
print("# Nr DE KG DE PAPA :",kg_papa," COSTO DE LA PAPA ES:",costo_papa)
print("# GANANCIA TOTAL   :",total)
print("###############################")
print("¿EL COMPRADOR ES COMPULSIVO?:",comprador_compulsivo)
