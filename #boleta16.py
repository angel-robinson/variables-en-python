#input
nombre=input("ingrese el nombre del cliente:")
celulares=float(input("ingrese la cantidad de los celulares:"))
precio_celulares=float(input("ingrese el precio:"))
#procesing
pago_total=precio_celulares*celulares
#vereficador
compro_celulares_r=(pago_total>=500)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# el cliente es            :",nombre)
print("# numero total de celulares:",celulares)
print("# precio de cada celular es:s/.",precio_celulares)
print("# pago total               :",pago_total)
print("###############################")
print("¿comprador magnifico ?:",pago_total)
