#Lista-----------------------------------------------------------------------------------------------------------
lista = ["Hola", "Javier", True, 1.89]
##print(lista)

#Acceder a un elemento de la lista por el indice
##print(lista[0])
##print(lista[3])

#Cambiar o modificar un dato de la lista
lista[3] = "comenzar"
##print(lista)

#Tupla (No se pueden modificar)----------------------------------------------------------------------------------
tupla = ("Hola", "Javier", True, 1.89)
##print(tupla)
##print(tupla[0])
##print(tupla[3])

#Conjunto (No se pueden modificar tampoco y no se peude acceder por su indice ya que los datos varian de posición y tampoco permite repetir datos-------------------------------------------------------------------------
conjunto = {"Hola", "Javier", True, 1.89, "Hola", 12, 45.8, "Todos"}
##print(conjunto)

#Diccionario-----------------------------------------------------------------------------------------------------
diccionario = {
    #key     : Value
    'nombre' : 'Juan Mendoza',
    'edad' : 34,
    'signo' : 'Geminis',
    'proyecto' : 'Aguas de corral',
    'universidad' : 'Cambridge UK',
    'soltero' : False
}

print(diccionario)
print(diccionario['universidad'])