#input
nombre=input("ingrese el nombre del cliente:")
numero_lapiceros=float(input("ingrese la cantidad de los lapiceros:"))
precio_lapiceros=float(input("ingrese el precio:"))
#procesing
pago_total=precio_lapiceros*numero_lapiceros
#vereficador
cantidad=(numero_lapiceros>10)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# el cliente es            :",nombre)
print("# numero total de lapiceros:",numero_lapiceros)
print("# precio de cada lapicero  :",precio_lapiceros)
print("# pago total               :",pago_total)
print("###############################")
print("¿invierte regular  en lapiceros ?:",cantidad)

