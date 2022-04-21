#esta funcion es de ORDEN SUPERIOR que nos permite trabajar con PARADIGMA de programacion FUNCIONAL (Python es un lenguaje de programacion MULTI-PARADIGMA , no solo es orientado a OBJETOS).
#Un filtro verifica que los elementos de una secuencia cumplen una condición, devolviendo un iterador con los elementos que cumplen dicha condición

#un primer ejemplo simple sería la creacion de una función que devuelva los números pares de una lista de números.

def numeroPar(x):
    if x % 2 == 0:
        return True

numeros=[27, 34,6,8,9,15,37]

print(list(filter(numeroPar, numeros)))  #usamos la función "list" para que alñ usar filter se visualice una lista y no una direccion. La función FILTER tiene dos parámetros: la función y la lista a la que aplicar dicha función
numerillospares=filter
#otra forma de hacerlo usando lambda (no seria necesaria la funcion numeroPar) sería:
print(list(filter(lambda y: y % 2==0, numeros)))

#aplicando filter a una lista de objetos

class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
    def __str__(self):
        return"{} ocupa el cargo de {} y su salario es de {}€".format(self.nombre, self.puesto, self.salario)

listaEmpleados=[
    Empleado("Angel", "Capataz", 30000),
    Empleado("Luisa", "Secretaria", 20000),
    Empleado("Marta", "Peón", 18000),
    Empleado("Veronica", "Oficial 1", 28000),
]

salarios_altos=filter(lambda individuo: individuo.salario>25000, listaEmpleados)

# print(list(filter(empleado.salario > 25000, listaEmpleados)))
for persona in salarios_altos:
    print(persona)

