#Para conseguir la PERSISTENCIA DE DATOS (conservacion de datos) se utilizan dos metodos: guardarlos en ARCHIVOS EXTERNOS o en BBDD. Las fases de creacion de un archivo externo son: creacion del archivo, apertura del archivo, manipulacion y cierre del archivo. Dos tipos de archivos: BINARIOS o DE TEXTO PLANO. Los que utilizaremos aqui son los segundos.

#Hay que utilizar el modulo IO de Python (ver la web docs.python.org en el apartado generic operating system services)

#en primer lugar abrimos el archivo con el método OPEN() del módulo IO. Ese método admite: lectura, escritura, append

from io import open

archivo_texto=open("archivo.txt","w") #abrimos un archivo con el nombre archivo.txt en modo escritura (indicado en el segundo parámetro "w"). Al ejecutar por primera vez esta línea de código se crea automáticamente un archivo con ese nombre en nuestro directorio de trabajo.

# Creamos el código que queremos incluir dentro de ese archivo.
frase = "Estupendo dia para estudiar Python \n el miércoles"

#Ahora lo incluimos:
archivo_texto.write(frase)

#Cerramos el archivo:
archivo_texto.close()

#ahora leemos lo que hay en el archivo y lo metemos en una variable que luego imprimimos
archivo_texto=open("archivo.txt","r")
texto=archivo_texto.read()
archivo_texto.close()
print(texto)

#tambien tenemos el método READLINES() lee línea a línea y almacena la info en una LISTA
archivo_texto=open("archivo.txt","r")
lineas_texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto)
print(lineas_texto[0])#accedemos a un elemento en concreto

#Agregar info al archivo
archivo_texto=open("archivo.txt","a")
archivo_texto.write("\n siempre es una buena ocasion para estudiar Python")
archivo_texto.close()
archivo_texto=open("archivo.txt","r")
texto=archivo_texto.read()
print(texto)

#usar un PUNTERO dentro de un fichero de texto. Cuando abrimos un fichero el puntero se coloca al inicio del archivo y cuando termina de leer se coloca al final del mismo. Si nos interesa modificar la posicion del puntero usamos el método SEEK() dando como parámetro la posición deonde se coloca el puntero. Por ejemplo el cursor, despues de leer el archivo se coloca al final y con la funcion SEEK(0) le decimos que se vuelva a colocar en la posicion inicial (0)
archivo_texto=open("archivo.txt","r")
texto=archivo_texto.read()
print(texto)
archivo_texto.seek(19)
texto=archivo_texto.read()
print(texto)
texto=archivo_texto.read(19)#con read hacemos una lectura HASTA el caracter 19
texto=archivo_texto.read()#esta lectura se hara desde la posicion 20 en adelante

archivo_texto.seek(len(archivo_texto.read())/2)#el puntero se posiciona a la mitad del texto
texto=archivo_texto.read()#lee desde la mitad del texto en adelante
print(texto)

#se puede indicar que el fichero sea de lectura y escritura con r+
archivo_texto=open("archivo.txt","r+") #el puntero esta al principio, asi que lo que introduzcamos se escribira alli
archivo_texto.write("Comienzo del texto: ") #sobreescribe lo que haya en el archivo desde el inicio hasta que se acabe esta cadena de texto y coloca el puntero al final del texto que introducimos
archivo_texto.seek(0) #tenemos que colocar el puntero al principio si queremos que lea todo el texto
texto=archivo_texto.read()
print(texto)

#otra forma seria usando WRITELINES().
archivo_texto=open("archivo.txt","r+")
lista_texto=archivo_texto.readlines()#genera un lista con las lineas de texto
lista_texto[1]="Esta linea la he cambiado desde fuera \n" #queremos cambiar la linea en la posicion 1 por esta linea
archivo_texto.seek(0)#el puntero se pone al principio
archivo_texto.writelines(lista_texto)
archivo_texto.seek(0)
texto=archivo_texto.read()
print(texto)
archivo_texto.close()
