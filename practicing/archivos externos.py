from io import open

from pyrsistent import v

archivo_temporal=open("practicing/archivo_permanente","wt")
texto_a_incluir="esto es una prueba de practica"
archivo_temporal.write(texto_a_incluir)
archivo_temporal.close()
archivo_temporal_para_lectura=open("practicing/archivo_permanente","rt")
texto_leido=archivo_temporal_para_lectura.read()
print(texto_leido)

import pickle

nombres=["tomas", "ana","ramiro","luisa"]

lista_temporal=open("practicing/listanombres","wb")

pickle.dump(nombres, lista_temporal)

lista_temporal.close()

del(lista_temporal)

lista_temporal2=open("practicing/listanombres","rb")

lista=pickle.load(lista_temporal2)

print(lista)


class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.frena=False
        self.acelera=False
    def arrancar(self):
        self.enmarcha=True
    def frenar(self):
        self.frena=True
    def acelerar(self):
        self.acelera=True
    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nArrancado: {self.enmarcha} \nFrenando: {self.frena} \nAcelerando: {self.acelera}")

coche1 = Vehiculo("Mazda","XCA200")
coche2 = Vehiculo("Seat","Arona")
coche3 = Vehiculo("VW","Passat")
coches=[coche1, coche2, coche3]

vehiculosTemporal=open("practicing/listaVehiculos", "wb")

pickle.dump(coches,vehiculosTemporal)

vehiculosTemporal.close()
del(vehiculosTemporal)

vehiculosTemporal=open("practicing/listaVehiculos","rb")
lista=pickle.load(vehiculosTemporal)
vehiculosTemporal.close()
for c in lista:
    print(c.estado())

