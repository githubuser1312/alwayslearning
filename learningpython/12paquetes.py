#PAQUETES son directorios en los que se almacenen los modulos que tienen relacion entre si.
#para crear un PAQUETE se crea una carpeta con un archivo que se llame __init__.py

#usando el paquete_calculos
from paquete_calculos.calculos_generales import *
from paquete_calculos.calculos_complicados.calculos_complicados import *

dividir(8,4)
redondear(5.6)
potencia(5,7)