#encontrar el area de un trapecio
#input
lado_mayor=float(input("ingrese lado mayor:"))
lado_menor=float(input("ingrese el lado menor:"))
altura=float(input("ingrese la altura:"))

#procesing
area_total=(lado_mayor+lado_menor)*altura/2

#vereficador
area_total_m=(area_total>=500)
#output
print("el area total del trapecio es:",area_total)
print("¿area total mayor que 500?",area_total_m)
