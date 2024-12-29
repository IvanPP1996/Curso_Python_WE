diccionario = {
    'nombre' : 'Thomas',
    'apellido' : 'Garcia',
    'edad' : 45,
    'casado' : True,
    'sueldo' : 4500000,
    'hijos' : False
}

#Métodos---------------------------------------------------------------------------------------------------------

#Método para mostrar la llave o key del diccionario
##print(diccionario.keys())

#Método para mostrar el valor de la llave o key del diccionario especificando su llave
##print(diccionario.get('sueldo'))

#Método para eliminar un diccionario especificando su llave
##diccionario.pop('nombre')
##print(diccionario)
##diccionario.pop('apellido', 'casado') #Forma de eliminar dos elementos
##print(diccionario)

#Método para iterar cada elemento del diccionario
print(diccionario.items())


#Método para eliminar un diccionario
##diccionario.clear()
##print(diccionario)
