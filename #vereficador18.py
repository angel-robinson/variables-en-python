#encontrar el diferencia de potencial
#input
intensidad_corriente=float(input("ingrese el la intensidad de corriente:"))
resistencia=float(input("ingrese el la resistencia:"))

#procesing
v=intensidad_corriente*resistencia
#vereficador
v_adecuado=(v>=48.3)
#output
print("el volumen es:",v)
print("¿la resistencia  es el adecuda para el cable?",v_adecuado)
