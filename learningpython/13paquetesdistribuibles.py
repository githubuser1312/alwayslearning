#DISTRIBUIR un paquete es hacer que ese paquete se pueda usar este donde esté. Es decir, si en un modulo usamos funciones que estan almacenadas dentro de un paquete y movemos ese paquete de directorio, ese módulo dejará de funcionar. Para evitar, que al mover el paquete de directorio deje de funcionar el programa usamos lo que se llaman PAQUETES DISTRIBUIBLES. Para ello lo que tenemos que hacer es incluir los paquetes dentro del propio Python.
#primeros creamos un fichero SETUP.PY
#siguiente paso, desde terminal en el directorio de trabajo, escribimos: 
#           $ python setup.py sdist    donde setup.py es nuestro archivo creado y sdist es la orden para crear paquete distribuible
# lo anterior nos crea dos archivos: paquetecalculos.egg-info y dist. En dist encontramos un archivo comprimido que es el paquete distribuible que podemos enviar donde queramos. Podemos instalarlo en el Python de nuestro ordenador y asi poder usar las funciones que contiene en cualquier modulo que creemos en cualquier directorio del ordenador. Para instalarlo en Python tenenos que ir al directorio DIST en nuestro terminal y escribir:
#           disr$ pip3 install paquetecalculos-1.0.tar.gz
# para ello hacemos un importacion normal y una llamada a la funcion a usar

#para desinstalar, dese cualquier directorio donde estemos:
#   $ pip3 uninstall paquetecalculos