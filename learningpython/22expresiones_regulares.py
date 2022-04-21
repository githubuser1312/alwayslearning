#las EXPRESIONES REGULARES o REGEX con como un MINIlenguaje de programacion dentro de un lenguaje de programación.
#Son una secuencia de caracteres que forman un patrón de búsqueda
#sirven para el trabajo y procesamiento de texto
#Ejemlos:
#buscar un texto que se ajusta a un formato determinado (email)
#buscar si existe o no una cadena de caracteres dentro de un texto
#contar el número de coincidencias dentro de un texto
#etc

import re

cadena="vamos a aprender expresiones regulares en Python. Además Python es un lenguaje de programcion sencillo"

print(re.search("aprender",cadena)) #en el método search de re el primer parámetro es la palabra que queremos buscar y el segundo es dóne queremos buscarlo. Esta funcion de vuelve la posicion y otros datos si encuentra el texto buscado y devuelve None si no lo encuentra. Para hacer algo más presentable podemos usar :

if re.search("aprender", cadena) is not None:
    print("He encontrado el texto")
else:
    print("no he encontrado el texto")


#para que nos de las posiciones donde comienza y termina el texto buscado usamos START, END o SPAN (que nos devuelve una tupla con los dos datos anteriores). Pero en primer lugar tenemos que almacenar la info que nos da re.search en una variable:
textoEncontrado=re.search("aprender", cadena)
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())

#para encontrar todas las palabras usamos FINDALL, por ejemplo buscar Python en cadena:
print(re.findall("Python", cadena))
# para que nos de la longitud de la lista que contiene Python:
print(len(re.findall("Python", cadena)))




# METACARACTERES________(caracteres comodín)_____ ANCHORS (anclas) y clases de caracteres____________

listas_varias=[
    'Ana Gómez',
    'María Martín',
    'Sandra López',
    'Santiago Martín',
    'Sandra Pérez',
    'niños',
    'niñas',
    'camión',
    'camion'
]

for elemento in listas_varias:
    if re.findall('^Sandra', elemento): #el caracter ^ indica que busque el elemento que EMPIEZA POR 
        print(elemento)
    elif re.findall('Martín$', elemento): #el caracter $ indica que busque el elemento que TERMINA POR 
        print(elemento)
    elif re.findall('z$', elemento): #el caracter $ indica que busque el elemento que TERMINA POR 
        print(elemento)
    elif re.findall('[rea]', elemento): #los corchetes [] indican que busque el elemento que CONTIENE esos caracteres independientemente del orden
        print(elemento)
    elif re.findall('niñ[oa]s', elemento): #los corchetes también nos sirven para abarcar varias posibilidades dentro de un elemento
        print(elemento)
    elif re.findall('cami[oó]n', elemento):
        print(elemento)




#RANGOS nos permiten buscar dentro de una lista elementos que contengan un RANGO de caracteres, números , etc

lista_nombres=[
    'Ana',
    'María',
    'Sandra',
    'Santiago',
    'Sandra',
]

for elemento in lista_nombres:
    if re.findall('[g-j]', elemento): #devuelve los nombres que CONTENGAN caracteres comprendidos en el rengo entre la o y la t (distingue entre mayúsculas y  minúsculas)
        print(elemento)
    elif re.findall('^[o-t]', elemento): #devuelve los nombres que EMPIECEN caracteres comprendidos en el rengo entre la o y la t (distingue entre mayúsculas y  minúsculas). E n este caso no devuelve ninguno
        print(elemento)
    elif re.findall('^[A-C]', elemento): #devuelve los nombres que EMPIECEN caracteres comprendidos en el rengo entre la o y la t (distingue entre mayúsculas y  minúsculas). E n este caso no devuelve ninguno
        print(elemento)


# otro ejemplo con numeros de pedidos, queremos saber que pedidos se han hecho entre el 3 y el 5 para ES (España)
lista_pedidos=[
    'PE_4',
    'CH_4',
    'ES_2',
    'US_3',
    'CH_2',
    'ES_4',
    'ES_5',
    'ES_6',
    'ES_A',
    'ES_B',
    'ES_C',

]
for pedido in lista_pedidos:
    if re.findall('ES_[3-5]', pedido):
        print(pedido)


#si queremos saber los pedidos que se han hecho para ES pero que NO sean los anteriores lo hacemos "NEGANDO" el RANGO con el uso de ^

for pedido in lista_pedidos:
    if re.findall('ES_[^3-5]', pedido):
        print(pedido)

#en el caso de que queramos que nos muestre varios pedidos de otro tipo, añadimos al rango aquellos caracteres que necesitamos:
for pedido in lista_pedidos:
    if re.findall('ES_[3-5A-B]', pedido):
        print(pedido)
