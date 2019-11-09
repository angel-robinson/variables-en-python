#encontrar el volumen de rectangulo
#input
lado1=float(input("ingrese el lado1:"))
lado2=float(input("ingrese el lado2:"))
altura=float(input("ingrese la altura:"))
#procesing
volumen=lado1*lado2*altura
#vereficador
volumen_l=(volumen>500)
#output
print("el volumen es:",volumen)
print("¿caben mas de 500 litros de agua?",volumen_l)
