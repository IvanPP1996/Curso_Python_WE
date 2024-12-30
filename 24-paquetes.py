import paquete.saludar

#Forma para mostrar que es un paquete y toca tener un archivo (__init__.py) para poder visualizar el paquete
##print(paquete.__path__)

#Forma de acceder a un paquete dentro de una carpeta o modulo
print(paquete.saludar.saludar('Diana'))