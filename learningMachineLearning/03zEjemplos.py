#===================== NUMPY ============================================================================================================================================================================================================================
import numpy as np
from sqlalchemy import column 

a = [[1,2], [1,2]]
b = [[1,0],[0,1]]
#a = [[1,2,3], [3,4,5], [6,7,8]]
#b = [[1,0,0],[0,1,0], [0,0,1]]
MatrixA = np.matrix(a)
MatrixB = np.matrix(b)

print(MatrixA * MatrixB)




#=================== PANDAS ============================================================================================================================================================================================================================



####### Series, ejemplos sencillos:

import pandas as pd 
s = pd.Series([1,2])#sin dar indices
print(s)

import pandas as pd 
s = pd.Series([1,2,3], index=['pack1', 'pack2', 'pack3'])#indicando los indices a usar
print(s)

####### Dataframe, ejemplos sencillos:

import pandas as pd 
d = pd.DataFrame([['Juan',23, 'alumno'],['Luisa',34, 'profesora'],['Tomás',56, 'alumno']])#crear un Dataframe CON LISTA, cabeceras de filas y columnas las pone automaticamente
print(d)

import pandas as pd 
d = pd.DataFrame([['Juan',23, 'alumno'],['Luisa',34, 'profesora'],['Tomás',56, 'alumno']], index=['persona01','persona02','persona03'], columns=['Nombre', 'Edad', 'Status'])
print(d)

import pandas as pd
d = pd.DataFrame({'Nombre': ['Juan', 'Luisa', 'Tomás'], 'Edad':[32,34,56], 'Status':['alumno', 'profesora', 'alumno']}, index=['persona01','persona02','persona03'], columns=['Nombre', 'Edad', 'Status']) #crear dataframe con diccionario
print(d)

import pandas as pd 
d = pd.DataFrame({'Marca': pd.Series(['Seat','VW', 'Lancia', 'Fiat', 'Renault'], index=['v01','v02','v03','v04','v05']), 'Precio': pd.Series([12000,11000,14500,18000], index=['v01','v02','v04','v05'])}) #crear dataframe con series de distintos tamaños


####### extraer datos de Series o Dataframe:

import pandas as pd 
s = pd.Series(['Audi', 'Seat', 'VW', 'Fiat', 'Dacia', 'Reanult', 'Mini'])
print(s[['1','2']])#por posicion
print(s[-1:])#por rango
print(s[1:3])#por rango
print(s[::-1])#por rango

import pandas as pd 
s = pd.Series(['Audi', 'Seat', 'VW', 'Fiat', 'Dacia', 'Reanult', 'Mini'],index=['v01','v02','v03','v04','v05','v06','v07'])
print(s)
print(s.loc['v03']) #por nombre/numero de fila
print(s.loc['v03','v04']) #por nombre/numero de fila
print(s.iloc[4])#por la posicion
print(s.iloc[2:4])#por rango

import pandas as pd 
d = pd.DataFrame({'Marca': ['Audi', 'Seat', 'VW', 'Fiat', 'Dacia', 'Reanult', 'Mini'], 'Precio': [20000,23000,30000,28000,40000,29000,19000]}, index=['v01','v02','v03','v04','v05','v06','v07'])
print(d[1:3])#por rango
print(d[::-1])#por rango
print(d['Marca']) #por columna
print(d.loc['v05','Marca'])#por nombre/numero de fila y columna
print(d.loc['v05'])#por nombre/numero de fila
print(d.iloc[2,1]) #por posicion unica
print(d.iloc[1:3]) #por rango filas
print(d.iloc[::-1])

####### filtrar datos

import pandas as pd 
s = pd.Series([20000,23000,30000,28000,40000,29000,19000], index=['precio01','precio02','precio03','precio04','precio05','precio06','precio07'])
d = pd.DataFrame({'Marca': ['Audi', 'Seat', 'VW', 'Fiat', 'Dacia', 'Reanult', 'Mini'], 'Precio': [20000,23000,30000,28000,40000,29000,19000]}, index=['v01','v02','v03','v04','v05','v06','v07'])

print(s[s>=25000]) #filtrar la serie por precio
print(s[s==25000]) #filtrar la serie por precio
print(d[d['Precio']>=25000])
print(d[d['Marca']=='Audi'])


####### visualizar datos 

import pandas as pd 
s = pd.Series([20000,23000,30000,28000,40000,29000,19000], index=['precio01','precio02','precio03','precio04','precio05','precio06','precio07'])
d = pd.DataFrame({'Marca': ['Audi', 'Seat', 'VW', 'Fiat', 'Dacia', 'Reanult', 'Mini'], 'Precio': [20000,23000,30000,28000,40000,29000,19000]}, index=['v01','v02','v03','v04','v05','v06','v07'])

print(s.describe())#imprime unna tabla resumen
print(d.describe())#imprime unna tabla resumen
print(s.head())#imprime las primeras 5 filas
print(s.tail())#imprime las útlimas 5 filas
print(s.tail())
print(d.head())
print(d.tail())
print(d.columns) #imprime nombre columnas

####### Datos NaN (no hallados)

import pandas as pd 

s1 = pd.Series(['Juan','Jose','Laura','Luisa','Rocio', 'Raquel'], index=['P01','P02','P03','P04','P05','P06'])
s2= pd.Series([20000,18000,32000,25000,14000],index=['P01','P02','P03','P04','P06'])
s3= pd.Series(["auxiliar","conductor","supervisora","oficial","peon"],index=['P01','P02','P03','P05','P06'])
d = pd.DataFrame({'Nombre':s1, 'Puesto':s3, 'Salario':s2})
print(d)
print(d.isnull()) #comprueba si hay valores NaN e imprime el DF (dificil de ver porque suele salir cortado)
print(d.fillna(0))#reemplaza los NaN por el valor que aparezca entre parentesis
print(d.dropna()) #elimina filas o columnas donde encuentre NaN

####### Borrar columnas de DataFrame

import pandas as pd 
d = pd.DataFrame({'Marca': ['Audi', 'Seat', 'VW', 'Fiat', 'Dacia', 'Reanult', 'Mini'], 'Precio': [20000,23000,30000,28000,40000,29000,19000]}, index=['v01','v02','v03','v04','v05','v06','v07'])
del d['Precio']
print(d)

####### Pop

import pandas as pd 
d = pd.DataFrame({'Marca': ['Audi', 'Seat', 'VW', 'Fiat', 'Dacia', 'Reanult', 'Mini'], 'Precio': [20000,23000,30000,28000,40000,29000,19000]}, index=['v01','v02','v03','v04','v05','v06','v07'])
print(d.pop('Marca'))
print(d)

####### Append

import pandas as pd 
d1 = pd.DataFrame({'Nombre': ['Tomás', 'Luis'], 'Edad':[23,34]})
d2 = pd.DataFrame({'Nombre': ['Roberto', 'Angel'], 'Edad':[32,28]})
d = d1.append(d2)
print(d)

####### Drop (elimina filas o columnas)

import pandas as pd 
d = pd.DataFrame({'Marca': ['Audi', 'Seat', 'VW', 'Fiat', 'Dacia', 'Reanult', 'Mini'], 'Precio': [20000,23000,30000,28000,40000,29000,19000]}, index=['v01','v02','v03','v04','v05','v06','v07'])
d1 = d.drop('v01')
print(d1)
d2 = d.drop(['v01','v03'])
print(d2)
d3 = d.drop(columns=['Precio'])
print(d3)


####### EJERCICIOS VARIOS DE: https://aprendeconalf.es/docencia/python/ejercicios/pandas/


'''Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.'''

import pandas as pd 
def ventas():
    years = ['2010','2011','2012','2013','2014']
    sells1 = []
    sells2 = []
    for y in range(0,len(years)): 
        sold = float(input('¿Qué ventas tuvo en {}?\n'.format(years[y])))
        sells1.append(sold)
        sells2.append(sold*0.9)
        print(sells1, sells2)
    sells_table = pd.DataFrame({'Ventas':sells1, 'Ventas con descuento':sells2}, index=years, columns=['Ventas','Ventas con descuento'])
    print(sells_table)
ventas()

'''Solución de la Web'''
import pandas as pd
inicio = int(input('Introduce el año inicial: '))
fin = int(input('Introduce el año final: '))
ventas = {}
for i in range(inicio, fin+1):
    ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': '))
ventas = pd.Series(ventas)
print('Ventas\n', ventas)
print('Ventas con descuento\n', ventas*0.9)



'''Escribir una función que reciba un diccionario con las notas de los alumno de un curso y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.'''

import pandas as pd 
def calificaciones(notas):
    n = pd.Series(notas)
    print(n.describe())
notas = {'Juan':6.5, 'Pedro':6.6, 'Maria': 8.3, 'Luisa':3.4, 'Roberto':9.3}
calificaciones(notas)

'''Soluciones de la Web'''
import pandas as pd
def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticos = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviación típica'])
    return estadisticos
notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
print(estadistica_notas(notas))

import pandas as pd
def estadistica_notas(notas):
    notas = pd.Series(notas)
    return notas.describe()
notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
print(estadistica_notas(notas))


'''Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.'''
import pandas as pd 
def aprobados(notas):
    s = pd.Series(notas)
    print(s[s>=5].sort_values(ascending=False))
notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5, 'Tomás':3.5}
aprobados(notas)


'''Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:'''
'''Mes :   Enero | Febrero | Marzo | Abril |'''
'''Ventas: 30500 | 35600   | 28300 | 33900 |'''
'''Gastos: 22000 | 23400   | 18100 | 20700 |'''

import pandas as pd 
datos = {'Mes':['Enero','Febrero','Marzo','Abril'],'Ventas':[30500, 35600, 28300, 33900],'Gastos':[22000, 23400, 18100, 20700]}
s = pd.DataFrame(datos)
print(s)



'''Escribir una función que reciba un DataFrame con el formato del ejercicio anterior, una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.'''

# mi solucion no es válida por que es el balance de todos los meses y no es eso lo que se pide
import pandas as pd 
datos = {'Mes':['Enero','Febrero','Marzo','Abril'],'Ventas':[30500, 35600, 28300, 33900],'Gastos':[22000, 23400, 18100, 20700]}
s = pd.DataFrame(datos)
def balance():
    ventas = s['Ventas'].sum(skipna=True)
    gastos = s['Gastos'].sum(skipna=True)
    b = ventas - gastos
    print(b)
balance()

#esta solucion la saco estudiando las dos siguientes
import pandas as pd 
datos = {'Mes':['Enero','Febrero','Marzo','Abril'],'Ventas':[30500, 35600, 28300, 33900],'Gastos':[22000, 23400, 18100, 20700]}
s = pd.DataFrame(datos)
def balance(s, meses):
    s['balance']=s['Ventas']-s['Gastos'] #añado una nueva columna en el dataframe con el balance
    s=s.set_index('Mes') #marco la columna de meses como la columna index (osea los nombres de filas)
    total=s.loc[meses,'balance'].sum() #localizo en el dataframe los meses que pasare por parámetro y hago la suma de sus balances
    print(total)
balance(s,['Enero', 'Marzo'])

'''Soluciones de la Web'''
import pandas as pd
datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ventas':[30500, 35600, 28300, 33900], 'Gastos':[22000, 23400, 18100, 20700]}
contabilidad = pd.DataFrame(datos)
def balance(contabilidad, meses):
    contabilidad['Balance'] = contabilidad.Ventas - contabilidad.Gastos
    return contabilidad[contabilidad.Mes.isin(meses)].Balance.sum()
print(balance(contabilidad, ['Enero','Marzo']))

import pandas as pd
datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ventas':[30500, 35600, 28300, 33900], 'Gastos':[22000, 23400, 18100, 20700]}
contabilidad = pd.DataFrame(datos)
def balance(contabilidad, meses):
    contabilidad['Balance'] = contabilidad.Ventas - contabilidad.Gastos
    return contabilidad.set_index('Mes').loc[meses,'Balance'].sum()
print(balance(contabilidad, ['Enero','Marzo']))


'''El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros). Construir una función que construya un DataFrame a partir del un fichero con el formato anterior y devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.'''

import pandas as pd 
def resumen_cotizaciones(fichero):
    df = pd.read_csv(fichero, sep=';', decimal=',', thousands='.', index_col=0)
    return pd.DataFrame([df.min(), df.max(), df.mean()], index=['Minimo', 'Maximo', 'Media'])

resumen_cotizaciones('learningMachineLearning/03zzCotizacion.csv')




'''El fichero 03zzTitanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:

    Generar un DataFrame con los datos del fichero.
    Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
    Mostrar por pantalla los datos del pasajero con identificador 148.
    Mostrar por pantalla las filas pares del DataFrame.
    Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
    Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
    Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
    Eliminar del DataFrame los pasajeros con edad desconocida.
    Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
    Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
    Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
'''

import pandas as pd 

fichero = 'learningMachineLearning/03zzTitanic.csv'
titan = pd.read_csv(fichero, sep=';', decimal=',', thousands='.', index_col=0)
print('Dimension: ', titan.shape)
print('Tamaño: ', titan.size)
print('Nombres de columnas :',titan.columns)
print('Nombres de filas :',titan.index)
print('Tipos de datos :',titan.dtypes)
print('Primeras 10 filas :',titan.head(10))
print('Ultimas 10 filas :',titan.tail(10))
print('Datos pasajero Id.148: ', titan.loc[148])
print('Datos filas pares ', titan.iloc[range(1,titan.shape[0],2)])
print('Personas en primera clase ', titan[titan['Pclass']==1].sort_values(by='Name'))
print('Porcentaje de sobrevivientes: ', titan[titan['Survived']==1].count()/titan['Survived'].count())
print('Porcentaje de muertos: ', titan[titan['Survived']==0].count()/titan['Survived'].count())
print('Porcentaje de sobrevivientes y muertos: ', titan['Survived'].value_counts()/titan['Survived'].count() * 100)
print('Porcentaje de sobrevivientes y muertos: ', titan['Survived'].value_counts(normalize=True) * 100)
print('Porcentaje de sobrevivientes por clase: ', titan.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100)
titan.dropna(subset=['Age'])
print('Edad media de las mujeres por clase: ', titan.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female'])
titan['Menor']=titan['Age']<18
print('Porcentaje de mayores y menores de edad que sobrevivieron y murieron por clase: ', titan.groupby(['Pclass','Menor'])['Survived'].value_counts(normalize=True) * 100)



'''Los ficheros 03zzEmisiones-2016.csv, 03zzEmisiones-2017.csv, 03zzEmisiones-2018.csv y 03zzEmisiones-2019.csv, contienen datos sobre las emisiones contaminates en la ciudad de Madrid en los años 2016, 2017, 2018 y 2019 respectivamente. Escribir un programa con los siguientes requisitos:

    Generar un DataFrame con los datos de los cuatro ficheros.
    Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc.
    Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una única columna.
    Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo datetime).
    Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy) y ordenar el DataFrame por estaciones contaminantes y fecha.
    Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.
    Crear una función que reciba una estación, un contaminante y un rango de fechas y devuelva una serie con las emisiones del contaminante dado en la estación y rango de fechas dado.
    Mostrar un resumen descriptivo (mínimo, máximo, media, etc.) para cada contaminante.
    Mostrar un resumen descriptivo para cada contaminante por distritos.
    Crear una función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones del contaminante indicado en la estación indicada.
    Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados para todos las estaciones.
    Crear un función que reciba una estación de medición y devuelva un DataFrame con las medias mensuales de los distintos tipos de contaminantes.
'''
import numpy as np
import pandas as pd
import datetime as dt

e1 = pd.read_csv('learningMachineLearning/03zzEmisiones-2016.csv', sep=';', decimal=',')
e2 = pd.read_csv('learningMachineLearning/03zzEmisiones-2017.csv', sep=';', decimal=',')
e3 = pd.read_csv('learningMachineLearning/03zzEmisiones-2018.csv', sep=';', decimal=',')
e4 = pd.read_csv('learningMachineLearning/03zzEmisiones-2019.csv', sep=';', decimal=',')
emisiones= pd.concat([e1,e2,e3,e4])
print(emisiones)

columnas=['ESTACION', 'MAGNITUD', 'ANO', 'MES']
columnas.extend([col for col in emisiones if col.startswith('D')])
emisiones = emisiones[columnas]
emisiones

emisiones = emisiones.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')
emisiones

# Crear una nueva columna con las fechas a partir del año, mes y día
# Primero eliminamos el caracter D del comienzo de la columna de los días
emisiones['DIA'] = emisiones.DIA.str.strip('D')
# Concatenamos las columnas del año, mes y día
emisiones['FECHA'] = emisiones.ANO.apply(str) + '/' + emisiones.MES.apply(str) + '/' + emisiones.DIA.apply(str)
# Convertimos la nueva columna al tipo fecha
emisiones['FECHA'] = pd.to_datetime(emisiones.FECHA, format='%Y/%m/%d', infer_datetime_format=True, errors='coerce')

# Eliminar las filas con fechas no válidas
emisiones = emisiones.drop(emisiones[np.isnat(emisiones.FECHA)].index)
# Ordenar el el dataframe por estación, magnitud y fecha
emisiones.sort_values(['ESTACION', 'MAGNITUD', 'FECHA'])

# Mostrar las estaciones disponibles
print('Estaciones:', emisiones.ESTACION.unique())
# Mostrar los contaminantes disponibles
print('Contaminantes:', emisiones.MAGNITUD.unique())

# Función que devuelve las emisiones de un contaminante dado en una estación y rango de fechas dado.
def evolucion(estacion, contaminante, desde, hasta):
    return emisiones[(emisiones.ESTACION == estacion) & (emisiones.MAGNITUD == contaminante) & (emisiones.FECHA >= desde) & (emisiones.FECHA <= hasta)].sort_values('FECHA').VALOR
evolucion(56, 8, dt.datetime.strptime('2018/10/25', '%Y/%m/%d'), dt.datetime.strptime('2019/02/12', '%Y/%m/%d'))

# Resumen descriptivo por contaminantes
emisiones.groupby('MAGNITUD').VALOR.describe()

# Resumen descriptivo por contaminantes y distritos
emisiones.groupby(['ESTACION', 'MAGNITUD']).VALOR.describe()

# Función que devuelve un resumen descriptivo de la emisiones en un contaminante dado en un estación dada
def resumen(estacion, contaminante):
    return emisiones[(emisiones.ESTACION == estacion) & (emisiones.MAGNITUD == contaminante)].VALOR.describe()

# Resumen de Dióxido de Nitrógeno en Plaza Elíptica
print('Resumen Dióxido de Nitrógeno en Plaza Elíptica:\n', resumen(56, 8),'\n', sep='')
# Resumen de Dióxido de Nitrógeno en Plaza del Carmen
print('Resumen Dióxido de Nitrógeno en Plaza del Carmen:\n', resumen(35, 8), sep='')

# Función que devuelve una serie con las emisiones medias mensuales de un contaminante y un mes año para todos las estaciones
def evolucion_mensual(contaminante, año):
    return emisiones[(emisiones.MAGNITUD == contaminante) & (emisiones.ANO == año)].groupby(['ESTACION', 'MES']).VALOR.mean().unstack('MES')

# Evolución del dióxido de nitrógeno en 2019
evolucion_mensual(8, 2019)




'''Datos IBEX35 desde Mayo2021 a Mayo2022, tratarlos con pandas y escribir líneas de código con las que se procese la informacion del archivo.'''
#importar bibliotecas
import pandas as pd 
import numpy as np 
#archivos csv 
enagas='learningMachineLearning/03zzENG35052021_0522.csv'
endesa='learningMachineLearning/03zzELE35052021_0522.csv'
repsol='learningMachineLearning/03zzREP35052021_0522.csv'
#crear dataframes desde los csv
df_enagas = pd.read_csv(enagas, sep=",", decimal='.')
df_endesa = pd.read_csv(endesa, sep=",", decimal='.')
df_repsol = pd.read_csv(repsol, sep=",", decimal='.')
#visualizar el dataframe de una de las empresas
print(df_enagas)
#por si acaso, comprobar si los tres dataframes tienen las mismas columnas con los mismos nombres en el mismo orden, para que luego podamos concatenarlas con seguridad
if np.array_equal(df_enagas.columns, df_endesa.columns) and np.array_equal(df_endesa.columns, df_repsol.columns):
    print('Todos los DF tienen las mismas columnas con los mismos nombres en el mismo orden')
else:
    print('Hay alguna diferencia entre las columnas de unas y otras')
#añadir una nueva columna al final con el nombre de la empresa
df_enagas['Name'] = 'Enagas'
df_endesa['Name'] = 'Endesa'
df_repsol['Name'] = 'Repsol'
#concatenar los 3 dataFrames y visualizar el nuevo dataFrame
df_energeticas = pd.concat([df_enagas, df_endesa, df_repsol])
print(df_energeticas)
print(df_energeticas.head(10))
print(df_energeticas.tail(10))
#tipos de datos del dataframe
print(df_energeticas.dtypes)
#cantidad de datos
print('Cantidad de datos del dataframe: ', df_energeticas.size)
#convertir la columna de Date a formato fecha (datetime)
df_energeticas['Date']=pd.to_datetime(df_energeticas['Date'], format='%Y-%m-%d')
print(df_energeticas.dtypes)
#comprobar si tenemos NaN en el nuevo Data Frame, devuelve False si no encuentra ningun valor
print(df_energeticas.isnull().value.any())
#no se ecuentra ningun NaN
#al concatenar los indices de la primera columna no nos vale porque se repiten en las 3 listados que hemos concatenados (por ejemplo la fila con el numero 3 está en enagas, repsol y endesa). Cambiamos la columna de esos indices por una nueva con indices desde la primera fila hasta la ultima correlativos.
#el numero de filas totales es de:
filas=df_energeticas.shape[0]
#creamos una lista con los que seran los nuevos índices:
a=[]
for i in range(0,filas):
    a.append(i)
#incluir una columnas con los que seran los nuevos indices
df_energeticas.insert(0,'column1',a)
print(df_energeticas)
#designar la nueva columna como la columna de los indices
df_energeticas=df_energeticas.set_index('column1')
print(df_energeticas)
#cambiamos el orden de algunas columnas
df_energeticas = df_energeticas[['Date', 'Open', 'Close', 'High', 'Low', 'Adj Close', 'Volume','Name']]
#Añadimos 2 columnas: 'Close-Open', 'High-Low'
df_energeticas.insert(3,'Close-Open',df_energeticas.Close - df_energeticas.Open)
df_energeticas.insert(6,'High-Low',df_energeticas.High - df_energeticas.Low)
#visualizar los datos generales del df
print(df_energeticas.describe())
#no necesitaremos la columna de precio ajustado al cierre de la bolsa, eliminamos la columna Adj Close
print(df_energeticas.columns)
#ahora borramos la columna
del df_energeticas['Adj Close']
#comprobamos que se ha borrado
print(df_energeticas.columns)
#que valores tenia enagas el 14 de Junio del 2021
df1 = df_energeticas[df_energeticas['Date'] == '2021-06-14']
df2 = df1[df1['Name'] == 'Enagas']
print(df2)
#todos los valores destacables por compañia
print(df_energeticas.groupby('Name').describe())
#valores máximos de volumen de acciones ejecutadas en un día de cada compañia
print(df_energeticas.groupby('Name')['Volume'].max())
#total de acciones vendidas durante ese periodo por compañía
print(df_energeticas.groupby('Name')['Volume'].sum())
#porcentaje del total de acciones vendidas que pertenecen a Repsol
print(df_energeticas[df_energeticas['Name'] == 'Repsol']['Volume'].sum() / df_energeticas['Volume'].sum() * 100)
#Por empresa cual fue la mayor perdida en valor por accion
print(df_energeticas.groupby('Name')['Close-Open'].min())



















