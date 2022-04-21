#las CLASES tienen: propiedades, estado y comportamiento(método)



class Coche():
    largoChasis=250     #propiedad1
    anchoChasis=120     #propiedad2
    ruedas=4            #propiedad3
    enmarcha=False      #propiedad4
    def arrancar(self): #una funcion dentro de una clase se llama metodo (definira el comportamiento del objeto) SELF indica el objeto al que hara alusion este método. En el ejemplo siguiente se refiere al objeto miCoche (miCoche=self)
        self.enmarcha=True #self.enmarcha = miCoche.enmarcha
    def estado(self): #este es otro comportamiento de la clase
        if self.enmarcha: #no hace falta poner =True porque se sobreentiende
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

miCoche = Coche()       #con esta linea lo que hacemos es INSTANCIAR una CLASE o EJEMPLARIZAR una CLASE

#para saber las propiedades o el comportamiento del objeto utilizamos la NOMENCLATURA DEL PUNTO. pe.: miCoche.largoChasis
print(f"El largo del coche es: {miCoche.largoChasis}")
print(f"El coche tiene {miCoche.ruedas} ruedas")
miCoche.arrancar() #en esta linea le decimos a la instancia u objeto que arranque
print(miCoche.estado()) #en esta linea le decimos que nos indique en que estado esta el objeto o instancia

#creamos un segundo objeto
print("------------ A continuacion creamos el segundo objeto ------------")

miCoche2 = Coche() #creamos la segunda estancia
print(f"El largo del coche es: {miCoche.largoChasis}") #la misma propiedad que el anterior
print(f"El coche tiene {miCoche.ruedas} ruedas") #la misma propiedad que el anterior
print(miCoche2.estado()) #este segundo objeto no ha arrancado

#otro ejemplo:
class robot():
    legs=2
    arms=2
    eyes=4
    wheels=2
    def post(self,position):
        if position=="s":
            return "it is sitting"
        elif position=="t":
            return "it is standing"
        elif position=="l":
            return "it still lying down"
    def physical_feat(self):
        return f"My robot has {self.legs} legs, {self.arms} arms, {self.wheels} wheels, {self.eyes} eyes"

miRobot=robot()
position=input("what is it doing right now?")
miRobot.post(position)
print(f"{miRobot.physical_feat()} and {miRobot.post(position)}")


#Un CONSTRUCTOR es un método especial que le da un "estado inicial" a los objetos y que se indica poniendo "__" delante y detras del nombre del método. En el ejemplo anterior todas las lineas referentes a las propiedades iniciales se escribirían (no olvidar "self"):
class robot():
    def __init__(self):
        self.legs=2
        self.arms=2
        self.eyes=4
        self.wheels=2
        self.start=False
    def started(self, starting):
        self.start=starting
        if self.start:
            return "it is started"
        else:
            return "it is not started"
       
    def physical_feat(self):
        return f"My robot has {self.legs} legs, {self.arms} arms, {self.wheels} wheels, {self.eyes} eyes"

miRobot2=robot()
print(f"{miRobot2.physical_feat()} and {miRobot2.started(True)}")

#ENCAPSULAMIENTO se usa para proteger una variable y que no se pueda cambiar desde FUERA de la clase (sí se puede cambiar desde dentro de la clase). En el ejemplo anterior podemos cambiar el numero de patas del robot desde fuera de la clase simplemente como se ve en las siguientes lineas:
class robot():
    def __init__(self):
        self.legs=2
        self.arms=2
        self.eyes=4
        self.wheels=2
    def post(self,position):
        if position=="s":
            return "it is sitting"
        elif position=="t":
            return "it is standing"
        elif position=="l":
            return "it still lying down"
    def physical_feat(self):
        return f"My robot has {self.legs} legs, {self.arms} arms, {self.wheels} wheels, {self.eyes} eyes"

miRobot3=robot()
position="l"
miRobot3.post(position)
miRobot3.legs=10
print(f"{miRobot3.physical_feat()} and {miRobot3.post(position)}")

#Para proteger las variables y que no se puedan modificar desde fuera usaremos "__" al principio de la variable:
class robot():
    def __init__(self):
        self.__legs=2
        self.__arms=2
        self.__eyes=4
        self.__wheels=2
    def post(self,position):
        if position=="s":
            return "it is sitting"
        elif position=="t":
            return "it is standing"
        elif position=="l":
            return "it still lying down"
    def physical_feat(self):
        return f"My robot has {self.__legs} legs, {self.__arms} arms, {self.__wheels} wheels, {self.__eyes} eyes"

miRobot4=robot()
position="l"
miRobot4.post(position)
miRobot4.legs=10 #aunque intentemos cambiar el valor d ela variable desde aqui, no podemos porque la variable está encapsulada 
print(f"{miRobot4.physical_feat()} and {miRobot4.post(position)}")

#tambien se puede hacer lo mismo con un método. Supongamos que el robot tiene que hacer un chequeo interno cuando le decimos que arranque. Si el chequeo interno (aceite es ok, bateria ok) da todo ok, entonces arranca (pero no tiene que volver a hacer un chequeo una vez realizado ese). Si no es todo ok, no arranca. El método del cheque interno no puede ser accesible desde el exterior de la clase (para evitar manipulacion de datos). Robot5 es un objeto de una clase en el que el autochecking no esta encapsulado y por lo tanto se puede acceder a el autochecking desde fuera (en el ejemplo llamamos otra vez al checking despues de haberlo hecho la primera vez al intentar arrancar el robot)

class robot():
    def __init__(self):
        self.__legs=2
        self.__arms=2
        self.__wheels=2
        self.__eyes=4
        self.__started=False
    def autochecking(self):
        print("Cheking levels...")
        self.oil="ok"
        self.battery="No ok"
        if self.oil=="ok" and self.battery=="ok":
            return True
        else:
            return False
    def starting(self, start):
        self.__started=start
        if self.__started:#esta linea simboliza la autocomprobacion que se hace de los niveles cuando se le da al boton de encendido, guardamos en una variable el diagnostico del chequeo
            checking=self.autochecking()
        if self.__started and checking:
            return "levels checked are ok, the robot is started"
        elif self.__started and checking==False:
            return "is trying to start but something is wrong with levels"
        else:
            return "is not started"
    def physical_feat(self):
        return f"My robot5 has {self.__legs} legs, {self.__arms} arms, {self.__wheels} wheels, {self.__eyes} eyes"

miRobot5=robot()
print(f"{miRobot5.physical_feat()} and {miRobot5.starting(True)}")
miRobot5.autochecking()

#en Robot6 no podemos llamar al autocheking desde fuera porque lo hemos encapsulado. Asi funciona correctamente.
class robot():
    def __init__(self):
        self.__legs=0
        self.__arms=4
        self.__eyes=1
        self.__started=False
    def __autochecking(self):
        print ("Checking levels....")
        self.oil="ok"
        self.battery="NO ok"
        if self.oil=="ok" and self.battery=="ok":
            return True
        else:
            return False
    def starting(self,start):
        self.__started=start #----!!!!!CUIDADO NO ES LO MISMO QUE start=self.__started¡¡¡¡¡¡¡-----
        if self.__started:
            autocheck_result=self.__autochecking()
        if start and autocheck_result:
            return "it is started"
        elif start and autocheck_result==False:
            return "it can not start because there are some issues with the oil or battery levels, Please check"
        else:
            return "it is not started"
    def features(self):
        return f"My robot6 has {self.__legs} legs, {self.__arms} arms, {self.__eyes} eye"
    
miRobot6=robot()
print(f"{miRobot6.features()} and {miRobot6.starting(True)}")
#miRobot6.__autochecking()#esta linea no se puede ejecutar y da error porque autochecking esta encapsulado



#HERENCIA
#en este ejemplo la clase moto lo hereda todo de la clase vehiculos ya demás hay que indicarle los dos parametros necesarios de marca y modelo que pide la clase vehiculos

class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        print (f"Marca : {self.marca} \nModelo : {self.modelo} \nArrancada : {self.enmarcha} \nAcelerando : {self.acelera} \nFrenando : {self.frena}")

class Moto(Vehiculos):
    pass

miMoto=Moto("YAMAHA", "XJ600")
miMoto.estado()

#SOBREESCRITURA DE METODOS en la herencia. Puede ocurrir que queramos añadir a uno de los metodos de la CLASE PADRE o SUPERCLASE algún método específico de la clase hija, como vemos en el ejemplo siguiente. En ese caso tenemos que volver a escribir el método original de la clase padre y hacer la modificación para la clase hija

class Vehiculos():
    def __init__(self, modelo, marca):
        self.modelo=modelo
        self.marca=marca
        self.arrancando=False
        self.acelerando=False
        self.frenando=False
    def arrancar(self):
        self.arrancando=True
    def frenar(self):
        self.frenando=True
    def acelerar(self):
        self.acelerando=True
    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nArrancado: {self.arrancando} \nFrenando: {self.frenando} \nAcelerando : {self.acelerando}")

class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito = "Haciendo el caballito"
    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nArrancado: {self.arrancando} \nFrenando: {self.frenando} \nAcelerando : {self.acelerando} \n{self.hcaballito}")

class vElectricos():
    def __init__(self):
        self.autonomia=100
    def cargar(self):
        self.cargando=True

class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if self.cargado:
            return "La furgoneta etá cargada"
        else:
            return "La furgoneta o está cargada"
        
class biciElectrica(vElectricos, Vehiculos):
    pass



miMoto2=Moto("HONDA", "CBR1000")
miMoto2.caballito()
miMoto2.estado()
miFurgo=Furgoneta("FORD","LUC")
print(miFurgo.carga(True))

#En el siguiente ejemplo un caso de HERENCIA MULTIPLE (tiene prioridad el "padre" del que hereda en primer lugar)

miBici=biciElectrica() #no podemos poner marca y modelo porque el padre principal es vElectricos y no tiene marca y modelo
#miBici.estado() # da error porque no tenemos marca y modelo


# Instruccion SUPER() llama al metodo de la clase padre (tenemos que darle los valores que requiere el INIT de la clase padre)

class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia
    def descripcion(self):
        print(f"Nombre : {self.nombre} \nEdad : {self.edad} \nResidencia : {self.lugar_residencia}")

class Empleado(Persona):
    def __init__(self, salario, antigüedad):
        self.salario = salario
        self.antigüedad = antigüedad

Antonio=Persona("Antonio",25,"Madrid")
Antonio.descripcion()

Antonio=Empleado(1500,15)
#Antonio.descripcion() da error porque no podemos darle los valores de nomnre, edad y residencia.

#Usando SUPER() resolvemos el problema de la herencia relativa a nombre, etc.:
class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia
    def descripcion(self):
        print(f"Nombre : {self.nombre} \nEdad : {self.edad} \nResidencia : {self.lugar_residencia}")

class Empleado(Persona):
    def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antigüedad = antigüedad
    def descripcion(self):
        super().descripcion()
        print(f"Salario : {self.salario} \nAntigüedad : {self.antigüedad}")

Luis=Empleado(1430,14,"Luis",26,"Sevilla")
Luis.descripcion()


#ISINSTANCE sirve para averiguar si un objeto pertenece a una instancia o no

print(isinstance(Luis, Empleado))
print(isinstance(Luis, Persona))
print(isinstance(Antonio, Empleado))



#POLIMORFISMO un objeto puede cambiar de forma dependiendo del contexto en el que se utilice. 

class Coche():
    def desplazamiento(self):
        print("Me desplazo usando 4 ruedas")
class Moto():
    def desplazamiento(self):
        print("Me desplazo usando 2 ruedas")
class Camion():
    def desplazamiento(self):
        print("Me desplazo usando 6 ruedas")

miVehiculo=Moto()
miVehiculo.desplazamiento()
miVehiculo2=Coche()
miVehiculo2.desplazamiento()
miVehiculo3=Camion()
miVehiculo3.desplazamiento()


#usando el POLIMORFISMO simplificamos:

class Coche():
    def desplazamiento(self):
        print("Me desplazo usando 4 ruedas")
class Moto():
    def desplazamiento(self):
        print("Me desplazo usando 2 ruedas")
class Camion():
    def desplazamiento(self):
        print("Me desplazo usando 6 ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Camion()
desplazamientoVehiculo(miVehiculo)#gracias al polimorfismo de Python esta funcion sabe que tiene que llamar a la funcion desplazamiento de la clase Camion()


#NOTA: la funcion especial __STR__ DE PYTHON se ve en 16guardadopermanente.py