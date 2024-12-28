#Declarando y definiendo una variable----------------------------------------------------------------------------
a = 5
b = 4
c = a + b
##print(c)

#Redefiniendo la variable----------------------------------------------------------------------------------------
nombre = 'Thomas Gomez'
nombre = 'Javier Fuentes'
nombre = 'Pedrito Perez'
##print(nombre)

#Concatenando----------------------------------------------------------------------------------------------------
nombre = 'Mario'
bienvenido = 'Hola ' + nombre + ' ¿Como andas loco?'
##print(bienvenido)

#Concatenando con f strings para convertir cualquier dato a texto de una vez
edad = 24
bienvenido = f'Hola {nombre} ¿Como andas loco? \nYa cumpliste los {edad} años verdad'
##print(bienvenido)

#Operador para borrar datos--------------------------------------------------------------------------------------
#del bienvenido
##print(bienvenido)

#Operador de pertenencia devuelve Boolean------------------------------------------------------------------------
print('ola' in bienvenido) #True
print('hola' in bienvenido) #False

print('ola' not in bienvenido) #False
print('hola' not in bienvenido) #True