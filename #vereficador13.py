#encontrar el area de circulo
#input
pi=float(input("ingrese el valor de pi:"))
radio=float(input("ingrese el radio:"))
#procesing
area_circulo=pi*radio**2
#vereficador
area_regular=(area_circulo>=25)
#output
print("el area es:",area_circulo)
print("¿el area del circulo es regular?",area_regular)
