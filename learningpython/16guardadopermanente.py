#guardar datos de forma permanente en ficheros
import pickle

class Persona():
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print(f"se ha creado una persona nueva con el nombre {self.nombre}")
    def __str__(self): #metodo especial de Python que convierte en cadena de texto la informacion
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class listaPersonas():
    personas=[]#lista en la que almacenaremos las personas que vayamos creando
    def __init__(self):
        listaDePersonas=open("ficheroExterno","ab+")#en el constructor incluimos una variable que representa el fichero que se abrira en memoria y que en realidad se guardara como "ficheroExterno" y que hara ab+ (append binary lectura y escitura)
        listaDePersonas.seek(0) #ponemos el cursor al principio
        try:
            self.personas=pickle.load(listaDePersonas)#nos dara error al principio porque al inicio no hay personas cargadas por ello tenemos que usar try
            print("se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)
    def agregarPersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    def mostrarInfoFicheroExterno(self):
        print("la info del fichero externo es la siguiente")
        for p in self.personas:
            print(p)


miLista=listaPersonas()#si solo ejecutamos esta linea nos saldra un mensaje que dice"El fichero esta vacio".

persona=Persona("Sandra","femenino","45")
miLista.agregarPersonas(persona)
persona=Persona("Maria","femenino","85")
miLista.agregarPersonas(persona)
persona=Persona("Eloisa","femenino","15")
miLista.agregarPersonas(persona)
persona=Persona("Antonio","masculino","18")
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()

# miLista.mostrarPersonas()