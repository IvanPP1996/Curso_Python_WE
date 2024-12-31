with open('archivo.txt','w', encoding="utf-8") as contenido:
    #Sobreescribiendo el archivo
    ##contenido.write('Nuevo texto ingresado para el sistema de computo')
    
    #Sobreescribiendo el archivo con mas contenido
    contenido.writelines([' - Nuevo texto ingresado para el sistema de computo','\n - Como andas maquina con este nuevo contenido del programaa rabbit'])
    contenido.writelines(['\n - Ahora como estas?','\n - tenemos mas información', '\n - Texto loco'])