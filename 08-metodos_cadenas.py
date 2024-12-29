cadena1 = "Hola a todos mis conocidos"
cadena2 = "bienvenido Loco"
numerico = "487756464"
alfanumerico = "holamundocomoestas"


#Funciones-------------------------------------------------------------------------------------------------------

#Funcion para conocer todos los metodos que se pueden aplicar
##print(dir(cadena1))
##print(dir(5))
##print(dir([1, "hola", 67.9, True]))

#Función para saber el largo de una cadena
##print(len(cadena1))

#Métodos---------------------------------------------------------------------------------------------------------

#Método para convertir todo a mayusculas
##print(cadena1.upper())
##print("hola monstruo como andas".upper())

#Método para convertir todo a minúscula
##print(cadena1.lower())

#Método para convertir la primera letra en mayuscula
##print(cadena2.capitalize())

#Método para encontrar un string o cadena dentro de otra cadena y devuelve la posición que este
##print(cadena1.find('Hola'))
##print(cadena1.find('a'))
##print(cadena1.find('z')) #Si no encuentra el valor nos devuelve -1

#Método para encontrar un string o cadena dentro de otra cadena y devuelve la posición que este la diferencia con find es que si no encuentra un valor este nos dara un error en vez de -1
##print(cadena1.index('Hola'))

#Método para saber si la variable de texto es númerico
##print(cadena1.isnumeric()) #False
##print(numerico.isnumeric()) #True

#Método para saber si la variable de texto es alfanúmerico
##print(cadena1.isnumeric()) #False
##print(alfanumerico.isnumeric()) #True (Solo si el valor esta entre la [Aa-Zz] y sin espacios)

#Método para saber cuantas veces se repite una cadena o concurrencia
##print(cadena1.count('a'))
##print(cadena1.count('o'))
##print(cadena1.count('Hola'))
##print(cadena1.count('z')) #Si no se encuentra muestra 0

#Método para saber si una cadena empieza con una cadena dada
##print(cadena1.startswith('H'))
##print(cadena1.startswith('Hola '))
##print(cadena1.startswith('h')) #False
##print(cadena1.startswith('U')) #False

#Método para saber si una cadena termina con una cadena dada
##print(cadena1.endswith('s'))
##print(cadena1.endswith(' conocidos'))
##print(cadena1.endswith('S')) #False
##print(cadena1.endswith('h')) #False

#Método para remplazar una cadena con otra cadena dada
cadena1_nueva = cadena1.replace('Hola', 'Adios')
##print(cadena1_nueva)

#Método para convertir una cadena a una lista o matriz
print(cadena1.split(" "))