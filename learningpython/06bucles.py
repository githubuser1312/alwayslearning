#por cada elemento de la lista o tupla se ejecuta el print y da igual que TIPO de elemento haya dentro de esa lista o tuple
for i in (1,2,3):
    print("hola")

for i in [1,2,3]:
    print("adios")

for i in ("a","b","c"):
    print("hola")

for i in ("a","b","c"):
    print(i)

for i in ("a","b","c"):
    print(i, end=" ")#imprime en una linea con un espacio entre ellos

for i in "ave":
    print("hola", end=" ")

#ejemplo de como varificar si es una direccion de correo comprobando si lleva @
su_email=input("Introduzca su email: ")
def emailcheck(su_email):
    email=False
    for i in su_email:
        if i == "@":
            email=True
    if email==True:
        print("su email es correcto")
    else:
        print("su email no es correcto")

emailcheck(su_email)
    
#ejemplo de como comprobar si es una direccion de correo al llevar @ y "."

su_email=input("Introduzca su email: ")
def emailcheck(su_email):
    email=0
    for i in su_email:
        if i == "@":
            email+=1
        if i == ".":
            email+=1
    if email==2:
        print("su email es correcto")
    else:
        print("su email no es correcto")

emailcheck(su_email)

#ese ejemplo ,lo podemos simplificar usand OR
su_email=input("Introduzca su email: ")
def emailcheck(su_email):
    email=0
    for i in su_email:
        if i=="@" or i==".":
            email+=1
    if email==2:
        print("su email es correcto")
    else:
        print("su email no es correcto")
emailcheck(su_email)

#RANGE() crea un array con lo que tiene dentro
for i in range(4):
    print("ole")

for i in range(4):
    print(i)

#con la funcion f podemos concatenar variables y textos añadiendo {}
for i in range(4):
    print(f"valor {i}")

#RANGE tiene los parametros inicial (donde comienza el rango), final (donde termina el rango) y salto (de cuanto en cuanto va subiendo)
for i in range(5, 12, 3):
    print(f"valor de la variable es {i}")

#ejemplo del email usando RANGE
su_email=input("Introduzca de nuevo su email: ")
def emailvalido(su_email):
    email_aceptado=False
    for i in range(len(su_email)):
        if su_email[i]=="@":
            email_aceptado=True
    if email_aceptado==True:
        print("Su email es correcto")
    else:
        print("Su email no es correcto, introduzcalo de nuevo")           
emailvalido(su_email)

#WHILE
i=1
while i<=10:
    print(f"Ejeucion {i}")
    i+=1 #esto es para que el bucle no sea infinito cuando llegue a 10 se parará
print("Termino la ejecucion")

#en el siguiente ejemplo nos preguntara la edad y si introducimos una edad negativa nos la volvera a preguntar y asi indefinidamente hasta que introduzcamos una edad positiva

edad=int(input("¿que edad tienes?: "))
while edad<0:
    print(f"edad incorrecta, por favor vuelve a introducir tu edad")
    edad=int(input("¿que edad tienes?: "))
print("gracias!")

edad2=int(input("¿Por favor, ¿que edad tienes?: "))
while edad2<18 or edad2>70:
    print(f"edad incorrecta, por favor vuelve a introducir tu edad")
    edad2=int(input("¿que edad tienes?: "))
print("gracias, puedes pasar!")

#determinar la raiz cuadrada de un numero pero admitiendo solo dos eerrores en la introduccion del numero del que hay qua hallar la raiz (el error es que sea un numero negativo)
import math
numero=int(input("Introduce el numero del que hallar la raiz cuadrada: "))
intentos=0

while numero<0:
    if intentos==2:
        print("lo has intentado tres veces. El programa ha finalizado")
        break
    print("el numero introducido es negativo, por favor introduce un numero positivo")
    numero=int(input("Introduce el numero del que hallar la raiz cuadrada: "))
    intentos+=1 #si pusieramos esta linea al principio, despues del while, solo tendriamos dos oportunidades, pero al colocarla aqui tenemos 3 oportunidades
if intentos<2:
    solucion=math.sqrt(numero)
    print(f"La raiz cuadrada de {numero} es {solucion}")    

#CONTINUE, PASS y ELSE

for letra in "Python":
    if letra=="h":
        continue #esa instruccion indica que se salte la siguiente linea y sigue el bucle desde el principio
    print(f"Viendo la letra {letra}")

#con la funcion CONTINUE contar el numero de letras de una frase (sin considerar los espacios en blanco)
nombre="Que bonito esta el cielo"
print(f"el numero de caracteres incluidos espacios es: {len(nombre)}")
n=0
for letra in nombre:
    if letra==" ":
        continue
    n+=1
print(f"Numero total de letras: {n}")
    
    
#PASS se usa para devolver un NULL
class MiClase:
    pass


#ELSE
email=input("Introduce tu email: ")
for i in email:
    if i == "@":
        arroba = True
        break
else:
    arroba=False
print(arroba)


