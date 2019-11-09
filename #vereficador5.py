#encontrar la fuerza rozamiento
#input
const_rozamiento=float(input("ingrese la fuerza de rozamiento:"))
normal=float(input("ingrese la fuerza normal"))
#procesing
fuerza_rozamiento=(const_rozamiento*normal)
#vereficador
fuerza_rozamiento_adecuda=(fuerza_rozamiento>=45)
#output
print("la fuerza ade rozamento es:")
print("¿la fuerxza de rozamiento es la adecuada?",fuerza_rozamiento_adecuda)
