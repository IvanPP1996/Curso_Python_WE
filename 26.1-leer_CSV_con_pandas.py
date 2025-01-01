#Importando libreria pandas
import pandas as pd

df = pd.read_csv("archivo.csv")
df2 = pd.read_csv("archivo.csv")
##print(df)

#Obteniedno solo datos de la columna nombre
##print(df["nombre"])

cadena = "0123456789"
#Método slicing para tener datos especificos desde un inicio hasta un final
##print(cadena[:3])
##print(cadena[:7])
##print(cadena[2:7])

#Ordenanado el archivo por edad de forma ascendente
def_ordenado_por_edad_asc = df.sort_values('edad')
##print(def_ordenado_por_edad_asc)

#Ordenanado de forma descendente
def_ordenado_por_edad_des = df.sort_values('edad',ascending=False)
##print(def_ordenado_por_edad_des)

#Conctenando los dos archivos
df_concatenado = pd.concat([df, df2])
##print(df_concatenado)

#Accediendo a las tres primeras filas con head
tercer_fila_inicio = df.head(3)
##print(tercer_fila_inicio)

#Accediendo a las tres ultimas filas con tail
tercer_fila_ultima = df.tail(3)
##print(tercer_fila_ultima)

#3Accediendo a la cantidad de filas y columnas con shape
##filas_y_columnas_totales = df.shape
##print(filas_y_columnas_totales)
#Usando desempaquetamiento
filas_totales,columnas_totales = df.shape
##print(filas_totales)
##print(columnas_totales)

#Obteniendo data estadística del dataframe (df)
df_info = df.describe()
##print(df_info)

#Accediendo a un elemento especiífico del df con loc
elemento_especifico = df.loc[2, "edad"]
##print(elemento_especifico)
#Accediendo a un elemento especiífico del df con iloc (Diferencia es que accedemos como si fuera por inidce y no nombre)
elemento_especifico = df.iloc[2, 2]
##print(elemento_especifico)

#Acediendo a todas las filas de una columna
apellidos = df.iloc[:,1]
##print(apellidos)
#Acediendo a la fila 3 de una columna esto tambien funciona igual con iloc
fila_3 = df.loc[2,:]
##print(fila_3)

#Accediendo a filas con edad mayor de 30
mayor_30 = df.loc[df['edad']>30,:]
print(mayor_30)