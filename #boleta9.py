#input
cliente=(input("ingrese le nombre del cliente :"))
aceite=int(input("ingrese el numero de aceite :"))
costo_aceite=float(input("ingrese el precio del aceite :"))
helados=int(input("ingrese el numero de helados:"))
costo_helado=float(input("ingrese el precio del helado :"))
#procesing
costo_total=(aceite*costo_aceite)+(helados*costo_helado)
#vereficador
comprador_insuficiente=(costo_total<10)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# EL CLIENTE ES :",cliente)
print("# Nr DE ACEITE  :",aceite,"  COSTO DEL ACEITE     :",costo_aceite)
print("# Nr DE HELADOS :",helados," COSTO DEL LOS HELADOS:",costo_helado)
print("# GANANCIA TOTAL:",costo_total)
print("###############################")
print("¿EL COMPRADOR ES INSUFICIENTE?:",comprador_insuficiente)
