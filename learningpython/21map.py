#MAP es una funcion de orden superior de python que aplica una función a cada elemento de una lista iterable (listas, tuplas, etc.) devolviendo una lista de resultados. ( diferencia con FILTER es que Filter aplica una Condicion y no una Funcion a cada elemento).

class Empleado():
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
    def __str__(self):
        return "{} ocupa el puesto de {} y su salario es de {}".format(self.nombre, self.puesto, self.salario)

listaEmpleados=[
    Empleado("Juan", "Gerente", 8000),
    Empleado("Maria", "directora", 5000),
    Empleado("Tomás", "administrativo", 3000),
    Empleado("Carmen", "Operaria", 2000),
    Empleado("Tania", "Peon", 1500),
    Empleado("Roman", "Seguridad", 2000)
]

#la funcion MAP usa como primer atributo una FUNCION (no una condicion como en el caso de FILTER) y como segundo atributo la lista sobre la que se aplicara dicha función.
#supongamos que queremos que cada empleado tenga un bonus en su sueldo de un 3%  y queremos saber el total que percibirá:

def bonus(empleado):
    empleado.salario = empleado.salario*1.03
    return empleado

listaBonusEmpleados=map(bonus,listaEmpleados)#creamos una lista donde almacenamos lo que crea la funcion MAP
for empleado in listaBonusEmpleados: #hacemos un for para ir imprimiendo cada empleado con sus valores
    print(empleado)


#otro ejemplo: queremos hacer lo mismo que antes pero el nuevo bonus solo se aplica a empleados con salarios menores o iguales a 2500 euros. Para ello revisaremos la funcion bonus:
def bonus2(empleado):
    if empleado.salario<=2500:
        empleado.salario = empleado.salario*1.05
    return empleado

listaBonusEmpleados=map(bonus2,listaEmpleados)#creamos una lista donde almacenamos lo que crea la funcion MAP
for empleado in listaBonusEmpleados: #hacemos un for para ir imprimiendo cada empleado con sus valores
    print(empleado)

