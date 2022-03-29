#en un DICCIONARIO los datos se almacenan asociando a una CLAVE un VALOR y no es necesario un irden de almacenamiento

miDiccionario={"Rusia":"Moscu", "España":"Madrid", "Francia":"Paris"}

#para determinar el Valor de una clave:
print(miDiccionario["Francia"])

#para imprimir un diccionario.
print(miDiccionario)

#agregar un elemento a un diccionario
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

#para corregir o cambiar el valor de una clave del diccionario se sobreesccribe
miDiccionario["Italia"]="Roma"
print(miDiccionario)

#para eliminar una pareja clave-valor se usa DEL
del miDiccionario["Italia"]
print(miDiccionario)

#usando tuplas para asignar claves a los valores
miTupla=("EEUU", "Argentina", "Chile")
miDiccionario2={miTupla[0]:"Washington",miTupla[1]:"Buenos Aires",miTupla[2]:"Santiago de Chile"}
print(miDiccionario2)

#un diccionario almacena una tupla o lista
miDiccionario3={1:"Luis",2:"Tomas",3:"Tomas",4:("Rebeca", "Carlos", "Ana")}
print(miDiccionario3)

mitupla5=("Rebeca", "Carlos", "Ana")
miDiccionario3={1:"Luis",2:"Tomas",3:"Tomas",4:mitupla5}
print(miDiccionario3)

milista5=["Rebeca", "Carlos", "Ana"]
milista5.append("Tatiana")
miDiccionario3={1:"Luis",2:"Tomas",3:"Tomas",4:milista5}
print(miDiccionario3)

#un dicionario almacena u diccionario con lista
miDiccionario4={1:"Luis",2:"Marta",3:"jorge",4:{"dipomas":["Tomas","Maria","Luisa"]}}
print(miDiccionario4)
print(miDiccionario4[4])

#KEYS devuelve las claves del diccionario
print(miDiccionario4.keys())

#VALUES devulve los valore de las claves
print(miDiccionario4.values())

#LEN devuelve la longitud del diccionario
print(len(miDiccionario4))