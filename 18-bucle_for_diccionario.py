diccionario = {
    'nombre' : 'Javier',
    'apellido' : 'Jhonson',
    'sueldo' : 8000000,
    'edad' : 34,
    'color' : 'rojo'
}

#recorriendo un diccionario pero mostrando solo sus llaves o claves
for key in diccionario:
    print(key)
#recorriendo un diccionario  mostrando sus llaves y valores
for key in diccionario.items():
    print(key)
    llave = key[0]
    valor = key[1]
    print(f'La clave es: {llave} y el valor es: {valor}')