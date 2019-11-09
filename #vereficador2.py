#encontrar la hiotenusa de un triangulo rectangulo
#input
cateto1=float(input("ingrese el primer cateto:"))
cateto2=float(input("ingrese el segundo cateto"))
#procesing
hipotenusa=(cateto1+cateto2)
#vereficador
hipotenusa_mayor_catetos=(hipotenusa>cateto1+cateto2)
#output
print("el valor de la hipotenusa es:",hipotenusa)
print("¿la hipotenusa es mayor que la suma de catetos?",hipotenusa_mayor_catetos)
