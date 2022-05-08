
#https://aprendeconalf.es/docencia/python/ejercicios/cadenas/

#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
nombre=input("¿Cuál es su nombre?: ")
n=int(input("Diga un número inferior a 10: "))
print((nombre + "\n") * n) #+ "\n" da un retorno de carro

#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
nombre=input("¿Cuál es su nombre?: ")
print("Su nombre es: "+ "\n" + nombre.lower() + "\n" + nombre.upper() + "\n" + nombre.title())
# title() pone todas las primeras letras en mayúscula, sin embargo capitaliza sólo pone la primera letra en mayúscula

#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
nombre=input("¿Cuál es su NOMBRE?: ")
print("Nombre: " + nombre.upper() + " tiene " + str(len(nombre)) + " letras.")
#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

numero_telefono=input("¿Cúal es su número de teléfono, incluido código de país y extensión (separados con guión)?")
x=numero_telefono.find("-")
y=numero_telefono.rfind("-")
print("Su número de teléfono sin prefijo ni extensión es: "+ numero_telefono[x+1:y] )
#solucion de la web
tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])

#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
frase=input("Introduzca una frase por consola: ")
print(frase[::-1])
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
frase=input("por favor introduzca una frase y una vocal en minúscula: ")
print(frase[:-1] + frase[-1:].upper())
#solucion de la web
frase=input("Introduce una frase: ")
vocal=input("¿qué vocal de la frase quieres poner en mayúscula?: ")
print(frase.replace(vocal, vocal.upper()))
#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
su_email=input("¿Cúal es su email?: ")
n=su_email.find("@")
dominio=su_email[n:]
print("Su nuevo email es: " + su_email.replace(dominio, "@ceu.es"))
#solucion de la web
su_email=input("¿Cúal es su email?: ")
print(su_email[:su_email.find("@")] + "@ceu.es")
#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
precio=input("¿Cúal es su precio (con dos decimales)?: ")
print(precio[:-3] + " euros " + precio[-2:] + " céntimos ")
#solucion de la web
precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
fecha=input("¿Cúal es su fecha de nacimiento (con formato dd/mm/aaaa)?: ")
print("Su fecha de nacimiento es el " + fecha[:fecha.find("/")] + " del mes " +  fecha[fecha.find("/")+1:fecha.rfind("/")] + " del año " + fecha[fecha.rfind("/")+1:] )
#solucion de la web
fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)
#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
#solucion1 de la web
cesta = input("Introduce los prductos de la cesta de la compra separados por comas: ")
print(cesta.replace(",", '\n'))
#solucion2 de la web
cesta = input("Introduce los prductos de la cesta de la compra separados por comas: ")
print("\n".join(cesta.split(",")))
print("1.".join(cesta.split(",")))
print(cesta.split(","))
#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
#solucion de la web
producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
unidades = int(input("Introduce las unidades del producto: "))
print('{pro}: {uni:3d} unidades x {pre:9.2f}€ = {total:11.2f}€  '.format(pro=producto, pre=precio, uni=unidades, total=precio * unidades))

