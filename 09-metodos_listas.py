lista = list(['hola', 'Dalto', 34, 56, 23, True])
lista_sin_cadenas = [2, 3, 87, False, 45, -9, 1, -78, 34, True, True]
##print(lista)

#Funciones-------------------------------------------------------------------------------------------------------

#Funcion para ver el largo de una lista
##print(len(lista))

#Métodos---------------------------------------------------------------------------------------------------------

#Método para agregar un elemento a la lista con append()
lista.append('jajajajajaja')
##print(lista)

#Método para agregar un elemento a la lista con insert() especificando un indice
lista.insert(2, False)
##print(lista)

#Método para agregar varios elementos a la lista con extend()
lista.extend(['Inicion', 'Final'])
##print(lista)

#Método para eliminar un elemento de la lista con pop() especificando un indice
lista.pop(0)
lista.pop() #Forma de eliminar el ultimo elemento o tambien agregando -1 y sguiendo asi se eleiminan al reves
##print(lista)

#Método para remover un elemento de la lista con remove() especificando su nombre
lista.remove(False)
##print(lista)

#Método para eliminar todos los elementos de la lista con clear()
lista.clear()
##print(lista)

#Método para ordenar todos los elementos de la lista en forma ascendente con sort() no debe tener cadenas de texto
#lista_sin_cadenas.sort()
##print(lista_sin_cadenas)
#lista_sin_cadenas.sort(reverse=True) #Orden descendente
##print(lista_sin_cadenas)

#Método para inveritr los elementos de una lista con reverse()
lista_sin_cadenas.reverse()
print(lista_sin_cadenas)
