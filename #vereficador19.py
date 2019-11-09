#encontrar aceleracion centripeta
#input
velocidad_tangencial=float(input("ingrese el lavelocidad tangencial:"))
radio=float(input("ingrese el radio:"))

#procesing
aceleracion_c=velocidad_tangencial**2/radio
#vereficador
aceleracion_c_adecuada=(aceleracion_c>=90)
#output
print("la acceleracion centripeta es:",aceleracion_c)
print("¿la acceleracion es la adecuada para que el movil no resbale?",aceleracion_c_adecuada)
