#Función simple
def saludar ():
    print('Hola amigo como andas')

##saludar()

#función con parametros
def saludar2 (nombre):
    print(f'Hola {nombre} como andas')

##saludar2('Jorge')

#Función que retorne valores
def contrasenia (num):
    lista_caracteres = 'abcdefghij'
    #num convertido a string
    num_entero = str(num)
    #Convertir a numero el primer digito
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasenia_digitada = f'{lista_caracteres[c1]}{lista_caracteres[c2]}{lista_caracteres[c3]}{num*2}'
    return contrasenia_digitada

##print(contrasenia(98))

#Función con parametro args (*)
def sumar (*numeros):
    return sum(numeros)
print(sumar(5,3,9,10,20,3))