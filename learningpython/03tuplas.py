#una TUPLA es una lista en la que no se puede cambiar nada (añadir, borrar) . Ventaja es que una TUPLA es más rápida que una LISTA y ocupa menos espacio en memoria que una LISTA. Se pueden utilizar como CLAVE en un DICCIONARIO (las LISTAS no)

# nombreTupla=(a,b,c,d,....)

#los elementos de una TUPLA pueden NO ir entre parentesis

miTupla=("Pedro",2,True)

#para extraer un valor de la tupla se usan cochertes, NO PARENTESIS
print(miTupla[2])

#para hacer una busqueda se usa INDEX igual que en Listas
print(miTupla.index(2))

#para convertir una Tupla en Lista se usa la funcion LIST
miLista=list(miTupla)
print(miLista)#al imprimir se ven los corchetes tipicos de una lista

#para convertir una tupla en Lista se usa TUPLE
miTupla2=tuple(miLista)
print(miTupla2)#al imprimir se ven los parentesis tipicos de la tupla

#para er si existe un elemento dentro de una tupla se usa IN
print("Pedro" in miTupla2)#imprime True

#con COUNT sabemos cuantas veces se encuentra un elemento dentro de una tupla
miTupla3=("a","d","f","d")
print(miTupla3.count("d"))

#con LEN sabemos la longitud de la tupla
print(len(miTupla3))

#tuplas unitarias llevan una COMA AL FINAL
miTupla4=("a",)

#EMPAQUETADO de tupla es escribir la tupla si parentesis
miTupla5="a",2,4,True #no es muy recomendable para evitar errores de confusion con variables

#DESEMPAQUETADO de tupla
miTupla6=("Ana",12,4,2022)
#creamos unas variables a las que se les asignará cada valor de la tupla al desempaquetarla
nombre,dia,mes,año=miTupla6
print(nombre)
print(año)
