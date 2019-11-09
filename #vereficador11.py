#encontrar el area de cuadrado
#input
lado1=float(input("ingrese el primer lado:"))
lado2=float(input("ingrese el segundo lado:"))

#procesing
area_total=lado1*lado2
#vereficador
area_total_m=(area_total>50)
#output
print(" el area total del cuadrado es:",area_total)
print("¿el area maxima es mayor que 50?",area_total_m)
