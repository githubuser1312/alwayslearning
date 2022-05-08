#https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/


#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad=int(input("¿Cúal es su edad?: "))
if edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
contraseña="contraseña"
seña = input("Contraseña a guardar: ")
if seña.lower() == contraseña:
    print("La contraseña es correcta")
else:
    print("La contraseña NO es correcta")
#solucion web
key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")

#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
num1=float(input("Introduzca primer número: "))
num2=float(input("Introduzca segundo número: "))
if num2 == 0:
    print("Error, no se puede dividir por 0")
else:
    print(num1 / num2)

#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
num1=int(input("Introduzca primer número: "))
if num1 % 2 == 0:
    print(f"El número {num1} es un número par")
else:
    print(f"El número {num1} NO es un número par")
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
edad=int(input("¿Qué edad tiene?: "))
ingresos=float(input("Sus ingresos mensuales: "))
if edad > 16 and ingresos >= 1000:
    print("Le corresponde tributar")
else:
    print("No le corresponde tributar")
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
sexo=input("¿Qué sexo tiene?, introduzca H para hombre y M para mujer: ")
nombre=input("¿Cuál es su nombre?: ")
if  sexo[0].upper() == "M" and nombre[0].upper() < "M" or  sexo[0].upper() == "H" and nombre[0].upper() > "N":
    print("Le corresponde el grupo A")
else:
    print("Le corresponde el grupo B")
#solucion de la web
name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if (gender == "M" and name.lower() < 'm') or (gender == "H" and name.lower() > 'n'):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group)
print(name.lower())

#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
'''Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%'''
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
renta=int(input("¿Cual es su renta anual?: "))
if renta < 10000:
    print("Su tipo impositivo es del 5%")
elif renta < 20000:
    print("Su tipo impositivo es del 15%")
elif renta < 35000:
    print("Su tipo impositivo es del 20%")
elif renta < 60000:
    print("Su tipo impositivo es del 30%")
else:
    print("Su tipo impositivo es del 45%")
#solucion de la web
# Preguntar al usuario por la renta
renta = float(input("¿Cuál es tu renta anual? "))
# Condicional para determinar el tipo impositivo dependiendo de la renta
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
# Mostrar por pantalla el producto de la renta por el tipo impositivo
print("Tienes que pagar ", renta * tipo / 100, "€", sep='')

#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
'''Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más'''
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
puntos=float(input("¿Cual es su puntuación?: "))
if puntos == 0.0:
    print('Su nivel es Inaceptable y su premio es de 0.0€')
elif puntos == 0.4:
    print(f'Su nivel es Aceptable y su premio es de {puntos * 2400}€')
else:
    print(f'Su nivel es Meritorio y su premio es de {puntos * 2400}€')
#solucion de la web
bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))
# Clasifiación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))

#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
edad=int(input("¿Cual es su edad?: "))
if edad < 4:
    print("Su entrada es gratis")
if edad < 18:
    print("Su entrada cuesta 5€")
else:
    print("Su entrada cuesta 10€")
#solucion de la web
edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
# Mostrar precio
print("El precio de la entrada es", precio, "€.")

#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
respuesta = input("¿Desea una pizza vegetariana? (S/N): ")
if respuesta == "S":
    ingrediente=input("¿Qué ingrediente desea? (Pimiento=P, Tofu=T):")
    if ingrediente.upper() == "P":
        print("Ha elegido una pizza vegetariana con Pimiento")
    else:
        print("Ha elegido una pizza vegetariana con Tofu")
else:
    ingrediente=input("¿Qué ingrediente desea? (Peperoni=P, Jamón=J, Salmón=S):")
    if ingrediente.upper()=="P":
        print("Ha elegido una pizza no vegetariana con Peperoni")
    elif ingrediente.upper()=="J":
        print("Ha elegido una pizza no vegetariana con Jamón")
    else:
        print("Ha elegido una pizza no vegetariana con Salmón")
#solucion de la web
# Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")