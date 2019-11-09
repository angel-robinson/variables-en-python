#input
nombre=input("ingrese el nombre del cliente:")
mesas=float(input("ingrese la cantidad de mesas:"))
precio_mesa=float(input("ingrese el precio:"))
#procesing
pago_total=precio_mesa*mesas
#vereficador
cantidad=(pago_total>100)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# el cliente es            :",nombre)
print("# numero total de lapiceros:",mesas)
print("# precio de cada lapicero  :",precio_mesa)
print("# pago total               :",pago_total)
print("###############################")
print("¿pago es mayor que 100 ?:",cantidad)
