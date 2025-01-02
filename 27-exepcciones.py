def sumar_dos():
    #Iniciando bucle
    while True:
        a = input('Número 1: ')
        b = input('Número 2: ')
        #Usando secuencia try para manejo de errores
        try:
            resultado = int(a) + int(b)
        except:
            print('Te pedí un número por favor ingresa de nuevo')
        #Si todo salio bien se genera el break para salir del bucle
        else:
            break
        #No es necesaria pero por saber siempre se ejecuta el finally si lo coloca
        finally:
            print('Esto siempre se va a ejecutar')
            
    return resultado

print(sumar_dos())