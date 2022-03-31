#SERIALIZACION es guardar un objeto, diccionario, etc en un archivo externo en CODIGO BINARIO. 
# Hay que usar la biblioteca PICKLE con sus dos métodos: DUMP() para volcar los datos al fichero binario y LOAD() para cargar los datos del fichero binario externo.

import pickle

from click import make_pass_decorator

lista_nombres=["Pedro", "ana", "Maria", "Isabel"]

fichero_binario=open("lista_nombres", "wb") #creamos fichero externo de nombre lista_nombres y del tipo wb (escritura binaria)

pickle.dump(lista_nombres, fichero_binario)#DUMP() tiene dos parametros la info que queremos volcar y le nombre del fichero "en memoria" (el fichero real es "lista_nombre")

fichero_binario.close()

del(fichero_binario)#lo eliminamos de memoria 


#con picle importado podemos ahora abrir el archivo para leer la informacion binaria (rb) que tiene el archivo (para ello lo metemos en un archivo en memoria que llamamos, en este ejemplo, "fichero")

fichero=open("lista_nombres","rb")

lista=pickle.load(fichero)#metemos la info en una variable al cargarla desde el archivo "fichero" que hemos abierto en memoria.

print(lista)

#SERIALIZACION DE OBJETOS (importanto pickle)

class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}")

#creamos los objetos
coche1=Vehiculo("Mazda","MX5")
coche2=Vehiculo("Seat","Altea")
coche3=Vehiculo("renault","megane")
#creamos la coleccion de objetos añadiendolos a una lista
coches=[coche1,coche2,coche3]

fichero=open("losCoches","wb")#abrimos en memoria un fichero "fichero" que se grabara con el nombre "losCoches" y que es de escritura binaria "wb"

pickle.dump(coches,fichero)#volcamos la info de la lista coches en "fichero" o lo que es lo mismo en el archivo real "losCoches"

fichero.close() #cerramos el fichero "fichero" que habiamos abierto en memoria para trabajar con el

del(fichero) #lo borramos de la memoria para que no ocupe memoria



#ahora recuperaremos la info del fichero "losCoches". IMPORTANTE: ESTO NO SE PUEDE HACER DESDE OTRO ARCHIVO (tiene que ser el mismo archivo donde se encuetre la clase "Vehiculo") a no ser que copiemos la clase "Vehiculo" en el nuevo archivo

fichero_apertura=open("losCoches", "rb")#abrimos el archivo recien creado para rb (lectura binaria)
leer_fichero=pickle.load(fichero_apertura)
fichero_apertura.close()#ya no necesitamos tener abierto en memoria fichero_apertura porque hemos cargado sus infor en la variable leer_fichero
for c in leer_fichero: #paraa leer la info usamos el bucle for
    print(c.estado())#si ponemos solo c no se entiende, pero si le aplicamos el método estado, nos imprime la info correctamente



