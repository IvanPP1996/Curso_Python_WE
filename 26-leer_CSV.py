#Importando libreria de CSV
import csv

with open("archivo.csv") as document:
    ##print('data leida correctamente')
    #Mostrar el contenido del archivo
    ##print(document.read())
    #Obtenidendo objeto csv.reader usando la libreria de CSV
    ##print(csv.reader(document))
    #Recorriendo un csv.roader para obtenerlo en forma de lista
    leer_todo = csv.reader(document)
    for row in leer_todo:
        print(row)