#https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

asignatura=[]
while True:
    a=input("nombre de asignatura :")
    if a == "fin":
        break
    asignatura.append(a)
    print(asignatura)
    
#solucion de la web
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(subjects)

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in subjects:
    print(f"Yo estudio {i}")
#solucion de la web
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for subject in subjects:
    print("Yo estudio " + subject)

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas=[]
for i in subjects:
    n=input(f"¿Qué nota has sacado en {i} ?")
    notas.append(n)
    print(notas)
for j in range(len(subjects)):
    print(f"En {subjects[j]} has sacado {notas[j]}")
#solucion de la web
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])


#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
loteria=[]
for i in range(6):
    loteria.append(input("¿Numeros ganadores de la loteria?: "))
loteria.sort()
print(loteria)
#solucion de la web
awarded = []
for i in range(6):
    awarded.append(int(input("Introduce un número ganador: ")))
awarded.sort()
print("Los números ganadores son " + str(awarded))

#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
lista=[]
for i in range(1,11):
    lista.append(i)
lista.sort(reverse=True)
print(lista)
#solucion de la web 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(numbers[-i], end=", ")
#solucion de la web 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
for number in numbers:
    print(number, end=", ")


#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
subjects1 = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
subjects2=[]
for i in subjects1:
    n=int(input(f"¿Qué nota has sacado en {i} ?"))
    if n < 5:
        subjects2.append(i)
print(subjects2)
#solucion de la web 1
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))

#solucion de la web 2
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(subjects)-1, -1, -1):
    score = float(input("¿Qué nota has sacado en " + subjects[i] + "?"))
    if score >= 5:
        subjects.pop(i)
print("Tienes que repetir " + str(subjects))

#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

#solucion de la web
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(alphabet), 1, -1):
    if i % 3 == 0:
        alphabet.pop(i-1)
print(alphabet)

#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
#solucion de la web
word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
vowels=['a','e','i','o','u']
word = input("Introduce una palabra: ")
numbers=[]
for i in vowels:
    x = word.count(i)
    numbers.append(x)
    print(f"la {i} aparece {x} veces")
print(numbers)
#solucion de la web
word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals: 
    times = 0
    for letter in word: 
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")
#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
precios=[50, 75, 46, 22, 80, 65, 8]
min = max = precios[0]
for precio in precios:
    if precio < min:
        min = precio
    elif precio > max:
        max = precio
print(f"el precio min es {min}")
print(f"el precio max es {max}")
       

#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
vector1 = (1,2,3)
vector2 = (-1,0,2)
producto=0
print(vector1[0]*vector2[0]+vector1[1]*vector2[1]+vector1[2]*vector2[2])
for i in range(len(vector1)):
    producto += vector1[i]*vector2[i]
print(f"el producto escalar de los vectores {vector1} y {vector2} es {producto}" )
#Escribir un programa que almacene las matrices
 
'''
A
=
(
1	2	3	
4	5	6 
)
y
B
=
(
−1	0	0	
1	1	1 
)

'''

#en una lista y muestre por pantalla su producto.Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
matrix1=((1,2,3),(4,5,6))
matrix2=((-1,0,0),(1,1,1))
producto =()
for i in range(len(matrix1)/2):
    a = 
#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.