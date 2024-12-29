diccionario = dict(nombre='Lucas', apellido='Torres', edad=34, sueldo=5000000)
##print(diccionario)

#Método para crear un diccionario con dos valores
diccionario_from_keys = dict.fromkeys('ABCD', 'apellido')
##print(diccionario_from_keys)
#Método para crear diccionario con fromKeys con resultado en cada clave como Nose
diccionario_from_keys = dict.fromkeys(['nombre', 'apellido', 'edad', 'sueldo'], 'Nose')
print(diccionario_from_keys)