#Creando mi propia exepcción
class MiExepcion(Exception):
    def __init__(self,err):
        print(f'Cometiste el siguiente error: {err}')

#Lanzando propia exepcción
##raise MiExepcion('ERROR algo salio mal')

#Manejando la propia exepcción
try:
    raise MiExepcion('ERROR algo salio mal')
except:
    print('Como vas a cometer ese error')
