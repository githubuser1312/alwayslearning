# A las funciones LAMBDA tambien se les llaman funciones : ON THE GO, ON DEMAND, ONLINE. Son funciones anonimas que resumen una funcion sencilla (para funciones complejas que tiene  bucles, condicionales, etc, NO SE PUEDEN USAR LAS FUNCIONES LAMBDA)

def area_triangulo(base,altura):
    return(base*altura)/2

#supongamos que queremos usarla varias veces

print(area_triangulo(5,8))


#la funcion anterior se puede resumir en:
area_triangulo2=lambda base,altura:(base*altura)/2

print(area_triangulo2(2,3))

#otro ejemplo
al_cubo=lambda numero:numero**3
print(al_cubo(3))

al_cubo2=lambda numero:pow(numero,3)
print(al_cubo2(3))


#otro ejemplo
destacar_valor=lambda comision:"¡{}! €".format(comision)

comision_Ana=15585

print(destacar_valor(comision_Ana))