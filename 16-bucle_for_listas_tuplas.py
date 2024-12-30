lista_animales = ['gato', 'perro', 'loro', 'cocodrilo']

##for animal in lista_animales:
##    print(animal)

lista_numeros = [10, 16, 14, 72, ]

##for num in lista_numeros:
##    print(num * 10)

#Función para iterar listas de manera interclada tambien se puede iterar mas de dos listas
##for animal, num in zip(lista_animales, lista_numeros):
##    print(f'Recorriendo lista 1 animales: {animal}')
##    print(f'Recorriendo lista 2 números: {num}')

#Función range() para iterar
#range(numero donde inicia, numero donde termina, constante de iteracion) NOTA: El número donde termina nunca lo coje en si por tal motivo hay que sumar 1 de mas es decir si quiero que termine en 10 debo ponerle 11
##for numero in range(5,10,2):
##    print(numero)

#Con dos parametros arranca del 5 al 9
##for numero in range(5,10):
##    print(numero)

#Con un parametro arranca del 0 al 19
##for numero in range(20):
##    print(numero)

#Recorriendo una lista con for forma no optima
##for num in range(len(lista_numeros)):
##    print(lista_numeros[num])

#Recorriendo una lista con for forma optima devolviendo el indice y el valor
for numero in enumerate(lista_numeros):
    print(numero)
    print(numero[0]) #Mostrar solo la llave o indice
    print(numero[1]) #Mostrar solo el valor de la llave
    
    indice = numero[0]
    valor = numero[1]
    print(f'El inidice es {indice} y su valor es {valor}')

#usando else este solo se muestra una vez
for num in lista_numeros:
    print(num)
else:
    print('El bucle termino')

#Forma corta en una línea de escribir for
lista_numeros = [2,4,6,8]
numeros_duplicados = [x*2 for x in lista_numeros] 
print(numeros_duplicados)