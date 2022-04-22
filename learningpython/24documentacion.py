#como adjuntar y ver la documentación/explicación que se adjunta en las funciones, clases, módulos, etc.??
# normalmente se usan las 3 comillas al principio y final de las explicaciones:

def potencia():
    '''esta operación da el resultado 
    fijo de exponenciar a 3
     el número 5'''
    print(pow(5,3))

class Operaciones():
    ''' Estas operaciones se 
    usan para bla blabla'''
    def suma(a,b):
        """ esta operacion hace la suma de solo dos 
        sumandos"""
        print(a+b)
    def resta(a,b):
        """" esta operación hace la resta de sólo
        dos números"""
        print(a-b)

potencia()
Operaciones.suma(3,4)
Operaciones.resta(9,3)

#para obtener la ayuda hay varios métodos (para ver el resultado, descomentar la linea de la que se quiera imprimir en terminal el resultado):
#print(potencia.__doc__)
#help(potencia) #esta da mas información
#help(Operaciones.suma)
#help(Operaciones) #da ayuda de la clase, en general.

#para verla explicacion de un módulo asociado a este archivo:

import modulos_metodos

help(modulos_metodos)