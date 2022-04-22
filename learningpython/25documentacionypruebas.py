#para hacer la prueba de una funcion, se escribe el comentario dentro de la funcion y 
#dentro del comentario se escribe la prueba que hay que realizar para ver si la
#funcion funciona correctamente o no. Para ello, la prueba debe comenzar con los simbolos >>>
# a continuación el nombre de la funcion con los parámetros a probar y en la siguiente linea
#el resultado correcto
#Mas adelante se IMPORTA el módulo DOCTEST y se le llama con la instruccion con: "doctest.testmod()"
#si no hay error, de acuerdo con el resultado esperado, la funcion no devuelve nada.
def areaTriangulo(base, altura):
    '''
    calula el área de un triángulo

    >>> areaTriangulo(5,2)
    5.0

    '''
    return(base*altura)/2
import doctest
doctest.testmod()
#en caso de que al hacer la prueba, el resultado no sea el que se ha especificado, 
# dara un error que se mostrará en el terminal
def areaTriangulo2(base, altura):
    '''
    calula el área de un triángulo

    >>> areaTriangulo2(5,2)
    7.0 

    '''
    return(base*altura)/2
import doctest
doctest.testmod()

#es muy IMPORTANTE especificar EXACTAMENTE lo que debe devolver la función, en el ejemplo siguiente se produce un error porque en el modo test NO SE HA especificado/añadido el texto que debe aparecer como parte de la solución de la función:
def areaTriangulo3(base, altura):
    '''
    calula el área de un triángulo

    >>> areaTriangulo3(5,2)
    5.0 

    '''
    return f"El área del triángulo es {(base*altura)/2}"
import doctest
doctest.testmod()

#el ejemplo anterior correcto sería, IMPORTANTE!!!!!!!!! para strings usar comillas simples (NO DOBLES):
def areaTriangulo4(base, altura):
    '''
    calula el área de un triángulo

    >>> areaTriangulo4(5,2)
    'El área del triángulo es 5.0'
    '''
    return f"El área del triángulo es {(base*altura)/2}"
import doctest
doctest.testmod()


#Se pueden hacer varias pruebas dentro de la función (y puede ocurrir que sólo una de las pruebas falle):
def areaTriangulo5(base, altura):
    '''
    calula el área de un triángulo

    >>> areaTriangulo4(5,2)
    'El área del triángulo es 5.0'

    >>> areaTriangulo4(6,2)
    'El área del triángulo es 6.0'

    >>> areaTriangulo4(9,3)
    'El área del triángulo es 13.5'
    '''
    return f"El área del triángulo es {(base*altura)/2}"

doctest.testmod()
#en el siguiente caso tiene sentido hacer varias pruebas
def compruebaMail(mailUsuario):
    '''
    Esta funcion comprueba que la direccion 
    de email tenga sólo una arroba y además no 
    puede estar al final de la dirección.
    >>> compruebaMail(pepe@google)
    True
    >>> compruebaMail(pepegoogle@)
    False
    >>> compruebaMail(pepegoogle)
    False
    '''
    arroba=mailUsuario.count('@')
    if arroba != 1 or mailUsuario.rfind('@')==len(mailUsuario)-1 or mailUsuario.find('@')==0:
        False
    else:
        True


