#Forma de abrir un archivo txt por python y usamos utf-8 para mostrar caracteres especiales
archivo = open("archivo.txt", encoding="utf-8")
##print(archivo.read())

#Forma para leer una línea por línea del código
##lineas = archivo.readlines()
##print(lineas)

#Forma para leer una línea específica del código
##linea_1 = archivo.readline()
##print(linea_1)
#Forma de leer caracteres de la línea
##linea_1 = archivo.readline(30)
##print(linea_1)

#Forma de cerrar el archivo despues de usarlo
archivo.close()
print(archivo.read()) #Vota un error para volverlo abrir toca hacerlo con open como en el principio
