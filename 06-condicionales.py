#Condicional if--------------------------------------------------------------------------------------------------
edad = 13
if edad >= 18:
    print('Puedes pasar')
else:
    print('No puedes pasar')

#Condicion if-else (elif)
ingreso_mensual = 800

if ingreso_mensual >= 10000:
    print('Estas bien economicamente en cualquier parte del mundo')
elif ingreso_mensual >= 1000:
    print('Estas bien economicamente en latinoameriica')
else:
    print('Sos pobre')

#If anidados
ingreso = 6000000
gasto = 4000000

if ingreso >= 5000000:
    if ingreso - gasto <= 0:
        print('Tus gastos son excesivos')
    elif ingreso - gasto >= 3000000:
        print('Tus gastos son accesibles y justos para ahorrar')
    else:
        print('Verifica si te alcanza a fin de mes')