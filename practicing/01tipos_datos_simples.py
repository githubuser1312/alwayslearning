#https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/

#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print('¡Hola Mundo!')
#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
saludo="¡Hola Mundo!"
print(saludo)
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
nombre=input("¿Cuál se su nombre de ususario?")
print(f"¡Hola {nombre}!")
#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética [(3+2)/(2x5)]sqrt2
def operacion():
    print(((3+2)/(2*5))**0.5)
operacion()
import math
def operacion2():
    print(math.sqrt((3+2)/(2*5)))
operacion2()
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
def salario():
    horas=int(input("¿Cuántas horas ha trabajado?"))
    coste=int(input("¿Qué coste hora tiene?"))
    print(f"La paga que le corresponde es de {horas*coste} euros")
salario()
#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: 
#suma= [n(n+1)/2]
def operacion3():
    n=int(input("Por favor, introduce un entero positivo: "))
    print(f"El resultado de la suma de todos lo enteros positivos desde 1 hasta {n} da como resultado: {(n*(n+1))/2} ")
operacion3()
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
def masa_corporal():
    peso = float(input("Por favor, introduzca su peso en kg: "))
    altura = float(input("Por favor, introduzca su altura en metros: "))
    imc = peso/altura**2
    print(f"Su Indice de Masa Corporal es de: {imc:.2f}")
masa_corporal()
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
def operacion4():
    n = int(input("Por favor introduzca un número: "))
    m = int(input("Por favor introduzca otro número: "))
    c = n//m
    r = n%m
    print(f"La división entera {n}/{m} da un cociente de {c} y un resto de {r}")
operacion4()
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
def capital_obtenido():
    c = float(input("¿Qué cantidad en euros desea invertir?: "))
    i = float(input("¿Cual es el interés anual en %?: "))
    n = float(input("¿Número de años?: "))
    capital_obtenido1 = c + (c * i/100 * n)
    capital_obtenido2 = c * ((1+(i/100)) ** (n))
    print(f"El capital obtenido en el caso de interés simple es de {capital_obtenido1:.2f} euros")
    print(f"El capital obtenido en el caso de interés compuesto es de {capital_obtenido2:.2f} euros")
capital_obtenido()
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
def peso_total():
    p_payasos = float(input("Número de payasos vendidos: "))*112
    p_muñecas = float(input("Número de muñecas vendidos: "))*75
    peso_total = (p_payasos + p_muñecas) / 1000
    print(f"El peso total del pedido es {peso_total} Kg")
peso_total()
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
def ahorros():
    c = float(input("Introduzca el capital inicial en euros: "))
    print(f"Los ahorros totales el primer año son de {round(c*((1+0.04)**1),2)} euros, el segundo año son de {round(c*((1+0.04)**2),2)} euros y el tercer año {round(c*((1+0.04)**3),2)} euros. ")
ahorros()
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
def pan():
    pan_de_antes=int(input("Número de barras de ayer: "))
    print(f"El precio de una barra de pan del dia es de 3.49€, el descuento por no ser fresa es de 60%. El coste total es de: {pan_de_antes * 3.49 * 0.6:.02f} ")

pan()