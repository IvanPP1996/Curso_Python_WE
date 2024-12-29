conjunto = set(['dato1', 'dato2'])
##print(conjunto)
conjunto = set(['dato1', ('datosub_1', 'datosub_2'), 'dato3'])
##print(conjunto)

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset({'dato1', 'dato2'})
conjunto2 = {conjunto1, 'dato3'}
##print(conjunto2)

#teoría de conjuntos (sub-conjuntos y super-conjuntos)
conjunto_super = {1,3,5,7,9,11}
conjunto_sub = {3,7,9}
conjunto_sub_2 = {2,4,6}

#Método para saber si es un subconjunto
resultado = conjunto_sub.issubset(conjunto_super)
#Forma 2
resultado = conjunto_sub <= conjunto_super
##print(resultado) # True
resultado = conjunto_super.issubset(conjunto_sub)
##print(resultado) # False

#Método para saber si es un superconjunto
resultado = conjunto_super.issuperset(conjunto_sub)
#Forma 2
resultado = conjunto_super >= conjunto_sub
##print(resultado) # True
resultado = conjunto_sub.issuperset(conjunto_super)
##print(resultado) # False

#Método para verificar si hay un elemento en común devuelve False si existe elemento en común
resultado = conjunto_sub.isdisjoint(conjunto_super)
print(resultado) #False
resultado = conjunto_sub_2.isdisjoint(conjunto_super)
print(resultado) #True