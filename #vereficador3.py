#encontrar la velocidad tangencial
#input
velocidad_angular=float(input("ingrese la velocidad angular:"))
radio=float(input("ingrese el radio:"))
#procesing
velocidad_tangencial=(velocidad_angular*radio)
#vereficador
velocidad_tangencial_regular=(velocidad_tangencial>velocidad_angular+radio)
#output
print("la velocidad tangencial es:",velocidad_tangencial)
print("¿la velocidad regular es la adecuada?",velocidad_tangencial_regular)
