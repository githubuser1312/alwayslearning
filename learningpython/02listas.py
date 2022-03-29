#las LISTAS en Python son como los vectores o arrays en otros programas. Nos permiten almacenar varios valores como una unidad.
#Las listas de Python nos permiten guardar diferentes tipos de valores
#Las listas se pueden expandir añadiendo nuevos elementos (arrays en otros programas no lo permiten)

#nombreLista = [a,b,c,....]

miLista=["Juan", "Luis", "Marta", "Jose"]

#para imprimir se incluyen los INDICES de los elementos
print(miLista[0])#ene ste caso imprime un elemento (no una lista)
print(miLista[0:2])
print(miLista[2:3]) #ene ste caso nos imprime una lista con un solo elemento
print(miLista[0:])
print(miLista[-3])#se pueden usar negativos para empezar desde el final de la lista
print(miLista[:3])#si no ponemos nada al principio se entiende que es 0 
print(miLista[2:])#imprime desde el indice 2 hasta el final

#la fucion APPEND añade 1 elemento a la lista (al final) 
miLista.append("Rebeca")
print(miLista[0:])

#para añadir varios elementos al mismo tiempo se usa EXTEND
miLista.extend(["Lucia","Eva","Sofia"])
print(miLista[0:])

#para añadir elementos en un lugar determinado de la lista se usa INSERT
miLista.insert(2,"Tomas")#inserta en la Lista en la posicion del indice 2
print(miLista[0:])

#para devolver el indice en el que esta un elemento:
print(miLista.index("Rebeca"))
#si hubiera elementos repetidos en la lista, index devolvería el indice del primer elemento encontrado en la lista.

#para ver si un elemento se encuentra o no en la lista usamos IN
print("Pepe" in miLista)#devuelve False porque no esta en la lista

#para eliminar elementos se usa REMOVE
miLista.remove("Rebeca")
print(miLista[0:])

#para eliminar el ultimo elemento de una lista con POP
miLista.pop()
print(miLista[0:])#elimina Sofia

#para concatenar listas podemos usar el operador +
miLista2=["Sandra", 23, True]
miLista3=[34,26,39,52]
miLista4=miLista+miLista2+miLista3
print(miLista4[0:])

#para repetir una lista un numero determinado de veces y generar una nueva lista con todas esas repeticiones tenemos el operador *
miLista5=miLista*3
print(miLista5[0:])

