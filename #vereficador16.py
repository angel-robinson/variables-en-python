#encontrar el volumen de una esfera
#input
pi=float(input("ingrese el valor de pi:"))
radio=float(input("ingrese el radio:"))

#procesing
volumen=pi*radio**3
#vereficador
volumen_r=(volumen>80)
#output
print("el volumen es:",volumen)
print("¿el volumen el mayor que 80?",volumen_r)
