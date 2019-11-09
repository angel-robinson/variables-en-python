#input
nombre=input("ingrese el nombre del cliente:")
computadoras=float(input("ingrese la cantidad de computadoras:"))
precio_computadoras=float(input("ingrese el precio:"))
#procesing
pago_total=precio_computadoras*computadoras
#vereficador
t_computadoras=(pago_total>5000)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# el cliente es                :",nombre)
print("# numero total de computadoras :",computadoras)
print("# precio de cada computadora es:s/.",precio_computadoras)
print("# pago total                   :",pago_total)
print("###############################")
print("¿llevo un ainversion mayor 5000 ?:",t_computadoras)
