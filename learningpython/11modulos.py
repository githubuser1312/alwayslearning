#podemos importar de dos formas:

# import modulos_metodos

# modulos_metodos.sumar(5,7)
# modulos_metodos.restar(5,3)


#para evitar tener que escribir modulos_metodos cada vez podemos importar todo usando el simbolo * (pero utiliza mas memoria) o importar solo las operaciones a usar 

from modulos_metodos import *
# from modulos_metodos import sumar, restar
sumar(5,7)
restar(6,3)
multiplicar(3,4)


