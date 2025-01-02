import re

texto = '''Hola como esta es la línea de texto 1.
¿esta es la línea de texto, 2 Hola?
esta es. La línea de ababababab texto, 3 23
Esta todo los ¡¡¡días!!!479 ,
Esta con abbb todas las 684747 posiblesabbbb. Causas del mundo'''

#Busqueda simple
resultado = re.search('Hola', texto)
##print(resultado)

#Busqueda de todos las concidencias en forma de lista
resultado = re.findall('Hola', texto)
##print(resultado)
#Agregando flags NOTA: re.IGNORECASE se usa para ingonorar si hay mayusculas o minsuculas
resultado = re.findall('esta', texto, flags=re.IGNORECASE)
##print(resultado)

#\d -> Busca digitos numéricos del 0 al 9
resultado = re.findall(r'\d', texto)
##print(resultado)

#\D -> Busca todo menos digitos numéricos del 0 al 9
resultado = re.findall(r'\D', texto)
##print(resultado)

#\w -> Busca caracteres alfanuméricos de [Aa-Zz] [0-9] [_]
resultado = re.findall(r'\w', texto)
##print(resultado)
#\W -> Busca todo menos caracteres alfanuméricos de [Aa-Zz] [0-9] [_]
resultado = re.findall(r'\W', texto)
##print(resultado)

#\s -> Busca espacios en blanco -> espacios, tabs, saltos de línea 
resultado = re.findall(r'\s', texto)
##print(resultado)
#\S -> Busca todo menos espacios en blanco -> espacios, tabs, saltos de línea 
resultado = re.findall(r'\S', texto)
##print(resultado)

#. -> Busca todo menos saltos de línea
resultado = re.findall(r'.', texto)
##print(resultado)

#\n -> Busca saltos de línea
resultado = re.findall(r'\n', texto)
##print(resultado)

#\ -> Cancela caracteres especiales, cancelando la función del punto y buscando puntos
resultado = re.findall(r'\.', texto)
##print(resultado)

#Armando una cedan que busque un número, seguido de un punto y espacio
resultado = re.findall(r'\d\.\s',texto)
##print(resultado)

#^ -> Buscando Hola al principio de una línea
resultado = re.findall(r'^Hola',texto)
##print(resultado)
#Aplicando flags NOTA re.M Buscar esta al comienzo de cada línea es decir activar multilínea
resultado = re.findall(r'^Esta',texto,flags=re.M)
##print(resultado)

#$ -> Buscar el final de cada línea
resultado = re.findall(r'mundo$',texto,flags=re.M)
##print(resultado)

#{n} -> Buscar n veces la cantidad del valor a la izquierda. Ejm: 345
resultado = re.findall(r'\d{3}\s',texto)
##print(resultado)

#{n,m} -> al menos n, como máximo m
resultado = re.findall(r'\d{2,4}',texto)
##print(resultado)
resultado = re.findall(r'ab{2,4}',texto)
##print(resultado)
resultado = re.findall(r'[ab]{2}',texto)
##print(resultado)

#| -> busca una cosa o la otra
resultado = re.findall(r'\d{2,4}|Hola',texto)
print(resultado)

