#encontrar el calor latente de fusion
#input
masa=float(input("ingrese la masa:"))
fusion=float(input("ingrese la fusion:"))

#procesing
q_fusion=(masa*fusion)
#vereficador
q_fusion_vapor=(q_fusion>740)
#output
print("el calor de fusion es es:",q_fusion)
print("¿el calor es el adecudo para que se evapore?",q_fusion_vapor)
