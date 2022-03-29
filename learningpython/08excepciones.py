#EXCEPCIONES son errores en tiempo de ejecucion debido a algo inesperado (no a un error de sintaxis)
#En el siguiente ejemplo haremos un CAPTURA o CONTROL de excepcion que lo que hara es que si se produce una excpcion, las lineas de programa que vengan a continuacion de la linea donde se ha producido el error, se puedan seguir ejecutando.
#Para examinar donde se ha producido el error examinamos la PILA DE LLAMADAS (donde se pueden ver donde se produce el error). Tambien debemos fijarnos en el nombre del tipo de error, p.e.: ZeroDivisionError. usamos TRY   EXCEPT para dar una opcion al programa en caso de que se presente el error.

#Ejemplo de operaciones matematicas (aprovechamos que la operacion 8/0 da el error ZeroDivisionError):

def suma(a,b):
    return a+b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "no se puede dividir por cero"

def multiplica(a,b):
    return a*b

def resta(a,b):
    return a-b

x=int(input("introduce el primer numero: "))
y=int(input("introduce el segundo numero: "))

operacion=input("elige una operacion: s para suma, r para resta, m para multiplica o d para divide: ")

if operacion=="s":
    print(suma(x,y))
elif operacion=="r":
    print(resta(x,y))
elif operacion=="m":
    print(multiplica(x,y))
elif operacion=="d":
    print(divide(x,y)) 
else:
    print("operacion no comtemplada") #esta linea de codigo es por si escribimos mal una operacion
print("a continuación vendria la ejecucion de otra parte del codigo")


#otro tipo de error: ValueError, solucion:

def suma(a,b):
    return a+b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "no se puede dividir por cero"

def multiplica(a,b):
    return a*b

def resta(a,b):
    return a-b

while True:
    try:
        x=int(input("OTRA VEZ introduce el primer numero: "))
        y=int(input("OTRA VEZ introduce el segundo numero: "))#si x o y no son correctos saltara a except sin pasar por break. Si son correcto pasara por break para terminar el while
        break 
    except ValueError:
        print("el valor introducido no es correcto, intentalo de nuevo")#en caso de que haya un error en los datos se vendra a esta linea y luego empezara el bucle while de nuevo 

operacion=input("elige una operacion: s para suma, r para resta, m para multiplica o d para divide: ").lower()

if operacion=="s":
    print(suma(x,y))
elif operacion=="r":
    print(resta(x,y))
elif operacion=="m":
    print(multiplica(x,y))
elif operacion=="d":
    print(divide(x,y)) 
else:
    print("operacion no comtemplada") #esta linea de codigo es por si escribimos mal una operacion
print("a continuación vendria la ejecucion de otra parte del codigo")


#otro ejemplo incluyendo las excepciones dentro de una funcion (FINALLY siempre se ejecutará)
def divide():
    try:
        x=float(input("VALOR DE LA X: "))
        y=float(input("VALOR DE LA Y: "))
        print(f'El valor de la division es: {x/y}')
    except ValueError:
        print("Elvalor introducido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    finally:
        print("cálculo finalizado")

#otro ejemplo seria con un except gemerico para todos los tipos de errores (aunque no es recomendable porque asi no se informa del tipo de error cometido)
# def divide():
#     try:
#         x=float(input("VALOR DE LA X: "))
#         y=float(input("VALOR DE LA Y: "))
#         print(f'El valor de la division es: {x/y}')
#     except:
#         print("Ha ocurrido un error")
#     finally:
#         print("cálculo finalizado")

#ejemplo de LANZAMIENTO DE EXCEPCIONES con la instruccion RAISE (que permite mensajes)
def evaluaEdad(edad):
    if edad<0:
        raise TypeError("NO se permiten edades negativas")
    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "eres joven"
    elif edad<65:
        return "eres maduro"
    elif edad<100:
        return "cuidate"
tuEdad=int(input("que edad tienes?: "))
print(evaluaEdad(tuEdad))

import math
def raizCuadrada(x):
    if x<0:
        raise ValueError("el numero no puede ser negativo")
    else:
        return math.sqrt(x)

num=int(input("introduce un numero para hallarle la raiz cuadrada: "))
print(raizCuadrada(num))
print("programa termiNado")

#en el ejemplo anterior, al introducir un numero negativo, salta una excepcion en la linea 127. Para solventarlo:
import math
def raizCuadrada(x):
    if x<0:
        raise ValueError("el numero no puede ser negativo")
    else:
        return math.sqrt(x)

num=int(input("VUELVE A INTRODUCIR un numero para hallarle la raiz cuadrada: "))
try:
    print(raizCuadrada(num))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
print("programa termiNado")
