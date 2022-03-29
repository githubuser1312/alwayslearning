#los objetos tienen: propiedades, estado y comportamiento(método)

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

#tambien se pued hacer lo mismo con un método. Supongamos que el robot tiene que hace run chequeo interno cuando le decimos que arranque. Si el chequeo interno (aceite es ok, bateria ok) da todo ok, entonces arranca. Si no es todo ok, no arranca. El método del cheque interno no puede ser accesible desde el exterior de la clase (para evitar manipulacion de datos).

