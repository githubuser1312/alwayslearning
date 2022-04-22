#son funciones que añaden funcionalidad a otras funciones que existan en nuestro programa, por eso se dice que decoran a otras funciones y son DECORADORES.
#la estructura esta formada por 3 funciones: A, B y C donde A recibe como parámetro una función B para devolver una función C. 
#un Decorador devuelve una función.

# def funcion_decorador(funcion):
    # def funcion_interna():<---------------------- FUNCION C
        #codigo de la funcion interna
    # return funcion_interna <---------------------- FUNCION C


#ejemplo de funcion decorador
#esta es la funcion decorador
def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        #acciones adicionales que decoran
        print("vamos a realizar un cálculo: ")
        funcion_parametro()
        #acciones adicionales que decoran
        print("se ha terminado el calculo")
    return funcion_interior
#estas son las funciones que queremos decorar
def suma():
    print(15+20)

def resta():
    print(40-10)
suma()
resta()

#ahora decoramos la primera funcion
@funcion_decoradora
def suma():
    print(15+20)

def resta():
    print(40-10)
suma()
resta()

#ahora decoramos la primera y segunda funcion
@funcion_decoradora
def suma():
    print(15+20)
@funcion_decoradora
def resta():
    print(40-10)
suma()
resta()

# ------------------------------ *ARGS  ------------------
#crear DECORADORES con PARÁMETROS: para ello usamos ------- "*args" ------- que es una convención en python que indica que se le pueden pasar un numero indeterminado de parámetros a la función (desde 1 en adelante). Se debe usar tanto en la función interior como en la función parámetro:
def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        #acciones adicionales que decoran
        print("vamos a realizar un cálculo: ")
        funcion_parametro(*args)
        #acciones adicionales que decoran
        print("se ha terminado el calculo")
    return funcion_interior

@funcion_decoradora
def suma(a,b,c):
    print(a+b+c)
@funcion_decoradora
def resta(a,b):
    print(a-b)
suma(50,23,5)
resta(70,32)

# ------------------------------ **KWARGS ---------------------
#en caso de que los parámetros sean del tipo CLAVE=VALOR se debe usar el parámetro ------- **kwargs --------
#supongamos que en el ejemplo anterior usamos una funcion portencia en la que los parámetros se concretan dando una pareja clave-valor:
def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):
        #acciones adicionales que decoran
        print("vamos a realizar un cálculo y el resultado es: ")
        funcion_parametro(*args, **kwargs)
        #acciones adicionales que decoran
        print("se ha terminado el calculo")
    return funcion_interior

@funcion_decoradora
def suma(a,b,c):
    print(a+b+c)
@funcion_decoradora
def resta(a,b):
    print(a-b)
@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(50,23,5)
resta(70,32)
potencia(base=2, exponente=3)