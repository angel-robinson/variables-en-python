#conversores tipo booleano
#convertir la cadena "3" a booleano
x="3"
a=bool(x)
print(a,type(a))
#convertir la cadena "angel" a booleano
x="angel"
a=bool(x)
print(a,type(a))
#convertir la cadena "38" a booleano
x="38"
a=bool(x)
print(a,type(a))
#convertir el enetero 8 a booleano
x=8
a=bool(x)
print(a,type(a))
#convertir real 0.0 a booleano
x=0.0
a=bool(x)
print(a,type(a))
#convertir el real 10.5 a booleano
x=10.5
a=bool(x)
print(a,type(a))
#convertir el booleano 1>=5 a booleano
x=(1>=5)
a=bool(x)
print(a,type(a))
#convertir el booleano 10<=10 a booleano
x=(10>=10)
a=bool(x)
print(a,type(a))
#convertir la cadena "0.5" a booleano
x="0.5"
a=bool(x)
print(a,type(a))
#convertir 20!=20 a booleano
x=(20!=20)
a=bool(x)
print(a,type(a))
#ejemplo de error
#convertir la cadena casa a booleano
x=casa
a=bool(x)
print(a)
