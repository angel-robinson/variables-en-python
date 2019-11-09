#encontrar el area de rectangulo
#input
base=float(input("ingrese la base:"))
altura=float(input("ingrese la altura:"))
#procesing
area_rectangulo=base*altura
#vereficador
area_regular=(area_rectangulo>=80)
#output
print("el area es:",area_rectangulo)
print("¿el area del rectangulo es la adecuada?",area_regular)
