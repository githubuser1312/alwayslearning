#https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/


#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
from itertools import count
from sre_constants import SRE_FLAG_ASCII


palabra=input("Escriba una palabra: ")
veces=[0,1,2,3,4,5,6,7,8,9]
for v in veces:
    print(palabra)
#solucion de la web
word = input("Introduce una palabra: ")
for i in range(10):
    print(word)

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad=int(input("Escriba su edad: "))
for e in range(1,edad+1):
    print(e)

age = int(input("¿Cuántos años tienes? "))
for i in range(age):
    print("Has cumplido " + str(i+1) + " años")
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
numero=int(input("Escriba un número entero positivo: "))
for e in range(1,numero+1,2):
    print(e, end=", ")
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
numero=int(input("Escriba un número entero positivo: "))
for e in range(numero,-1,-1):
    print(e, end=", ")

#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
#INTERES COMPUESTO
capital=float(input("Capital a invertir: "))
interes=float(input("Interes anual: "))
años=int(input("A cuantos años: "))
for i in range(1,años+1):
    print(str(round(capital*(1+interes/100)**i,2)))
#solucion de la web
amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))

#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
'''
*
**
***
****
*****
'''
numero=int(input("Escriba un número entero positivo: "))
for i in range(numero+1):
    print("*"*i)
#solucion de la web
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")
#otra solucion de la web
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
   print("*"*(i+1))
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range(1,11):
    for j in range(1,11):
        print(j*i,end=" ")
    print()
#solucion de la web
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

'''
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''
numero=int(input("Escriba un número entero positivo: "))
for i in range(1,numero+1,2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()


#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
password="correct"
passw=input("Escriba su contraseña: ")
while password!=passw:
    passw=input("La contraseña no era correct, por favor escriba su contraseña: ")
print("la contraseña introducida es correcta")
#solucion de la web
key = "contraseña"
password =""
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")

#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
#solucion web 1
n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")
#solucion web 2
n = int(input("Introduce un número entero positivo mayor que 2: "))
for i in range(2, n):
    if n % i == 0:
        break
if (i + 1)  == n:
    print(str(n) + " es primo")
else: 
    print(str(n) + " no es primo")
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
word = input("Introduce una palabra ")
for i in range(1,len(word)+1):
    print(word[-i],end=" ")
#solucion de la web
word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input("Introduce una frase")
letra = input("Introduce una letra")
x = frase.count(letra)
print(f"La letra {letra} está {x} veces en la frase")
y=0
for i in range(1,len(frase)):
    if letra == frase[i]:
        y+=1
print(f"La letra {letra} se encuentra {y} veces en la frase que has escrito")
#solucion de la web
frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
frase=""
while frase != "salir":
    frase = input("Introduce una frase: ")
    print(frase)
print()
#solucion de la web
while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)