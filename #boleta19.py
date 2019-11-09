#input
cliente=input("ingrese el nombre del cliente:")
billetera_n=float(input("ingrese la cantidad de billeteras:"))
precio_billeteras=float(input("ingrese el precio:"))
#procesing
pago_total=billetera_n*precio_billeteras
#vereficador
pago_total_billetera=(pago_total>=500)
#output
print("###############################")
print("# BOLETA DE VENTA ")
print("#")
print("# el cliente es               :",cliente)
print("# numero total de billeteras :",billetera_n)
print("# precio de cada billetera es :s/.",precio_billeteras)
print("# pago total                  :",pago_total)
print("###############################")
print("¿comprador excelente ?:",pago_total_billetera)
