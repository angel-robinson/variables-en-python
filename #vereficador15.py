#encontrar el volumen de un cubo
#input
lado1=float(input("ingrese el lado1:"))
lado2=float(input("ingrese el lado2:"))
altura=float(input("ingrese la altura:"))
#procesing
volumen=lado1*lado2*altura
#vereficador
volumen_adecuado=(volumen>=40)
#output
print("el volumen es:",volumen)
print("¿el volumen del cubo es el adecudo?",volumen_adecuado)
