#el objeto PALABRAS se llaman CADENAS - STRINGS y en Python tienen muchos métodos.

# upper()=todo en mayusculas
# lower()= todo en minusculas
# capitalize() = pone en mayuscula la primera Letra de la PRIMERA palabra de una frase
# title() = pone en mayuscula la primera Letra de una palabra o de CADA palabra de una frase
# count()=cuenta cuantas veces se repite una letra o grupo de letras
# find()= da el indice donde se encuentra la letra o grupo dentro de una cadena
# isdigit()= devuelve True o False (es o no un numero o no)
# isalum()= comprueba si son alfanumericos
# isalpha()= comprueba si hay solo letras (no cuenta los espacios)
# split()= separa por palabras usando espacios
# strip()=borra los espacios sobrantes al principio y al final
# replace()=cambia palabra o letra por otra
# rfind()= hace lo mismo que find() pero contando desde atras

#EN ESTA PAGINA TENEMOS UN LISTADO CON MAS DETALLE: https://docs.python.org/es/3/library/stdtypes.html#text-sequence-type-str

nombreUsuario=input("Introduce tu nombre de usuario: ")
print(f"el nombre es {nombreUsuario.upper()}")
print(f"el nombre es {nombreUsuario.capitalize()}")

edad=input("Introduce tu edad: ")
while edad.isdigit()==False:
    print("por favor introduce un valor numerico")
    edad=input("Introduce tu edad: ")
            
if int(edad)<18:
    print("no puedes pasar")
else:
    print("puedes pasar")
    

