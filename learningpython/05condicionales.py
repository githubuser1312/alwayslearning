#condicional IF
def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(6))
print(evaluacion(3))

#INPUT(), admite parámetros
print("programa de evaluacion de alumnos")
nota_alumno = int(input("La nota del alumno ha sido: ")) #añado int para indicar que el valor sera un integer (si no daria error) 
def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion
print(evaluacion(nota_alumno))


#ELSE()
print("ACCESS PERMISSION")
edad_solicitante=int(input("¿cual es tu edad?:"))
def acceso(edad):
    if edad >= 18:
        print("Access granted")
    else:
        print("Acces denied")
acceso(edad_solicitante)

#ELIF()
print("Calificacion")
nota_alumno=float(input("¿cual es tu nota?:"))#cambio int a float para admitir numeros con decimales (pe.: 4.5)
def acceso(nota):
    if nota<5:
        print("insuficiente")
    elif 5<=nota<6:
        print("suficiente")
    elif 6<=nota<7:
        print("bien")
    elif 7<=nota<9:
        print("notable")
    else:
        print("sobresaliente")
acceso(nota_alumno)

#IN, OR, AND

#en este ejemplo se tienen que cumplir 3 condiciones
distancia_al_cole=float(input("La distancia al colegio es:"))
hermanos_hermanas=int(input("¿Cuantos herma@s tiene?: "))
ingresos_anuales=int(input("¿Cuales son los ingresos totales de la familia? :"))

def beca(distancia,hermanos,ingresos):
    if distancia>40 and hermanos>2 and ingresos<=20000:
        print("Se le concede la beca")
    else:
        print("Se le deniega la beca")
beca(distancia_al_cole,hermanos_hermanas,ingresos_anuales)

#en este ejemplo se tienen que cumplir dos de las condiciones o una de las tres que tiene mas importancia
distancia_al_cole=float(input("La distancia al colegio es:"))
hermanos_hermanas=int(input("¿Cuantos herma@s tiene?: "))
ingresos_anuales=int(input("¿Cuales son los ingresos totales de la familia? :"))

def beca(distancia,hermanos,ingresos):
    if distancia>40 and hermanos>2 or ingresos<=20000:
        print("Se le concede la beca")
    else:
        print("Se le deniega la beca")
beca(distancia_al_cole,hermanos_hermanas,ingresos_anuales)

#en este ejemplo vemos el uso de IN (en este ejemolo usamos lower() para el caso en que el input se haga con mayusculas)
print("Asignaturas para el año 2020")
print("Asignatura optativas:lengua,matematicas,historia.")
asignatura_elegida=input("Asignatura elegida: ").lower()
def eleccion_asignatura(asignatura):
    asignaturas=("lengua", "matematicas", "historia")
    if asignatura in asignaturas:
        print("Su asignatura elegida es: " + asignatura)
    else:
        print("La asignatura elegida no se encuentra entre las disponibles, por favor eliga una de las disponibles")
eleccion_asignatura(asignatura_elegida)