#Importando un modulo a otro modulo
##import modulos_saludar
##print(modulos_saludar.saludar('Lucas'))

#Al usara as nos permite definir un nombre para el modulo que importamos
##import modulos_saludar as m_saludar
##print(m_saludar.saludar('Lucas'))

#Importar funciones del modulo y les cambiamos el nombre
from modulos_saludar import saludar as bienvenido, saludar_raro as rarete
print(bienvenido('Juan Pablo'))
print(rarete('Frank'))