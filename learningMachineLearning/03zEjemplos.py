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
print(s.head())
print(s.tail())
print(d.head())
print(d.tail())
print(d.columns)

####### Datos NaN (no hallados)

import pandas as pd 

s1 = pd.Series(['Juan','Jose','Laura','Luisa','Rocio', 'Raquel'], index=['P01','P02','P03','P04','P05','P06'])
s2= pd.Series([20000,18000,32000,25000,14000],index=['P01','P02','P03','P04','P06'])
s3= pd.Series(["auxiliar","conductor","supervisora","oficial","peon"],index=['P01','P02','P03','P05','P06'])
d = pd.DataFrame({'Nombre':s1, 'Puesto':s3, 'Salario':s2})
print(d)
print(d.isnull())
print(d.fillna(0))
print(d.dropna())

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