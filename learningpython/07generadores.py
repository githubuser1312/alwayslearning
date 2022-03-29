#comparar una FUNCION normal con un GENERADOR que usa YIELD con el siguiente ejemplo. Aparentemente son muy similares.

limitedelista=int(input("Dime el limite de la lista: "))
def generaPares(limite):
    i=1
    listapares=[]
    while i<=limite:
        listapares.append(2*i)
        i+=1
    return listapares

print(generaPares(limitedelista))


limitedelista=int(input("Dime el limite de la lista: "))
def generaPares(limite):
    i=1
    while i<=limite:
        yield i*2
        i+=1

devuelvePares=generaPares(limitedelista) 
for i in devuelvePares:
    print(i)

#pero un GENERADOR usa menos espacio en memoria porque solo genera la informacion que se pide en ese momento. En el siguiente ejemplo el GENERADOR solo usara espacio en memoria para cada numero que se imprima y NO para la lista completa de numeros pares que se generaria si usaramos una funcion normal.
#usamos NEXT para devolver el siguiente valor de la lista (el primer NEXT devuelve el primer valor e la lista)

limitedelista=int(input("Dime el limite de la lista: "))
def generaPares(limite):
    i=1
    while i<=limite:
        yield i*2
        i+=1

devuelvePares=generaPares(limitedelista) 

print(next(devuelvePares))
print("Aqui habria mas codigo....")
print(next(devuelvePares))
print("Aqui habria mas codigo....")
print(next(devuelvePares))
print("Aqui habria mas codigo....")

#YIELD FOR se usa para funciones anidadas

def devuelve_ciudades(*ciudades):#el asterisco significa que va a recibir un numero indeterminado de elementos y los recibira en forma de tupla
    for elemento in ciudades:
        yield elemento

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Sevilla","Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

#Si anidamos tendriamos:
def devuelve_ciudades2(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento

ciudades_devueltas2=devuelve_ciudades2("Madrid","Barcelona","Sevilla","Valencia")

print(next(ciudades_devueltas2))
print(next(ciudades_devueltas2))

#usando YIELD FROM se simplifica la funcion y el resultado es igual al anterior
def devuelve_ciudades3(*ciudades):
    for elemento in ciudades:
            yield from elemento

ciudades_devueltas3=devuelve_ciudades3("Madrid","Barcelona","Sevilla","Valencia")

print(next(ciudades_devueltas3))
print(next(ciudades_devueltas3))