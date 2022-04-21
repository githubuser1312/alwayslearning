#Pasos a seguir para conectar con BBDD:
    # 1) Abrir-Crear conexión
    # 2) Crear puntero o cursor
    # 3) Ejecutar query (consulta SQL)
    # 4) Manejar los resultados de la query (consulta): insertar, leer, actualizar, borrar ( CRUD, create read updatate)
    # 5) Cerrar puntero
    # 6) Cerrar conexión

#USO DB Browser for SQlite para ver las tablas y bbdd creadas en los siguientes ejemplos


#Usamos SQlite3
import sqlite3

#como no esta creada la bbdd, la creamos sobre la marcha con nombre "PrimeraBase"

miConexion=sqlite3.connect("PrimeraBase")#Primer paso de Crear conexión

miCursor=miConexion.cursor() #Segundo paso creacionde puntero o cursor

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") #lo que hay dentro de los paréntesis es lenguaje SQL (se estudia aparte). Con este paso se ha creado la tabla , aunque sigue vacía. IMPORTANTE¡¡¡¡¡¡¡¡¡¡¡, ESTA LINEA HAY QUE INVALIDARALA DESPUES DE EJECUTARLA LA PRIMERA VEZ, SI NO NOS DARA ERROR.

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')") #con esta insertamos un solo producto. Comentamos despues de insertarlo para que cuando volvamos ha ejecutar este programa no nos de error.

#Para insertar varios productos al mismo tiempo:
variosProductos=[
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Cerámica"),
    ("Camión", 20, "Juguetería"),
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos )
miCursor.execute("SELECT * FROM PRODUCTOS") #para consultar
variosProductos=miCursor.fetchall() #coge la lista completa de productos y en una siguiente linea la imprimimos para verla en terminal
print(variosProductos)#imprimo una lista completa de productos
for producto in variosProductos: #imprimo por separado cada producto 
    print(producto)
for producto in variosProductos: #imprimo sólo el nombre de cada artículo con su precio y donde esta en el supermercado
    print(f"El artículo {producto[0]} tiene un precio de {producto[1]} euros y está en la sección de {producto[2]}")

miConexion.commit()#despues de hacer un cambio en la tabla, hay que CONFIRMAR que queremos hacer ese cambio por eso se hace el commit

miConexion.close()#paso 6 cerrar conexión, sólo con el paso 1 y este último se crea la base de datos aunque este vacía

#OTRA BBDD____________________________________________________________________________
miConexion2=sqlite3.connect("GestionProductos")
miCursor2=miConexion2.cursor()
#a continuación los campos de la tabla incluyendo PRIMARY KEY  que indica el campo clave IMPORTANTE: EL CAMPO CLAVE NO SE SE PUEDE REPETIR
# miCursor2.execute('''
#     CREATE TABLE PRODUCTOS2(
#         CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
#         NOMBRE_ARTICULO VARCHAR(50),
#         PRECIO INTEGER,
#         SECCION VARCHAR(20)
#     )
# ''')
# productos2=[
#     ("AR01", "pelota", 10, "juguetaría"),
#     ("AR02", "pantalón", 20, "confección"),
#     ("AR03", "destornillador", 24, "ferretería"),
#     ("AR04", "jarrón", 45, "cerámica")
# ]
# miCursor2.executemany("INSERT INTO PRODUCTOS2 VALUES (?,?,?,?)", productos2)
# miCursor2.execute("INSERT INTO PRODUCTOS2 VALUES ('AR05', 'TREN', 15, 'JUGUETERIA') ") #insertamos un nuevo articulo con diferente valor de codigo articulo
#si intentamos insertar un nuevo articulo con el mismo codigo key que otro de los que ya estan dentro de la bbdd, nos dara una error del tipo UNIQUE (integrityerror)


#CAMPO CLAVE AUTOMATICO______________________________________________________
#para no tener que preocuparse de insertar un cmapo clave, lo haremos asi (añadimos ID integer y autoincrement en la linea donde se incluye el primary key):

# miCursor2.execute('''
#     CREATE TABLE PRODUCTOS2(
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NOMBRE_ARTICULO VARCHAR(50),
#         PRECIO INTEGER,
#         SECCION VARCHAR(20)
#     )
# ''')

productos2=[
    ("pelota", 10, "juguetaría"),
    ("pantalón", 20, "confección"),
    ("destornillador", 24, "ferretería"),
    ("jarrón", 45, "cerámica")
]
miCursor2.executemany("INSERT INTO PRODUCTOS2 VALUES (NULL,?,?,?)", productos2)#IMPORTANTE: HAY QUE ELIMINAR UNA DE LAS 4 INTERROGACIONES QUE PUSIMOS EN EL CASO ANTERIOR Y EN SU LUGAR INTRODUCIR NULL



#UNIQUE________________________________________________________________________
#si queremos asignar a un campo la clave UNIQUE para que no se pueda repetir en ningun otro elemento de la BBDD haremos AGREGANDO UNIQUE al campo que no se puede repetir (UNIQUE se aplicaria por ejemplo al campo DNI de una lista de personal)
miConexion3=sqlite3.connect("GestionProductos3")
miCursor3=miConexion3.cursor()
# miCursor3.execute('''
#     CREATE TABLE PRODUCTOS3(
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#         PRECIO INTEGER,
#         SECCION VARCHAR(20)
#     )
# ''')
productos3=[
    ("pelota", 10, "juguetaría"),
    ("pantalón", 20, "confección"),
    ("destornillador", 24, "ferretería"),
    ("jarrón", 45, "cerámica")
]
# miCursor3.executemany("INSERT INTO PRODUCTOS3 VALUES (NULL,?,?,?)", productos3)
#intentemos crear ahora un producto con el mismo nombre de otro de la bbdd
# miCursor3.execute("INSERT INTO PRODUCTOS3 VALUES (NULL, 'pelota', 12, 'juguetería')")
#es intento nos da un error IntegrityError: UNIQUE constraint failed.
#añado otro producto similar pero no igual y no da problemas
# miCursor3.execute("INSERT INTO PRODUCTOS3 VALUES (NULL, 'pantalones', 12,'confección')")



#LEER - READ___________________________________________________________________________
miCursor3.execute("SELECT * FROM PRODUCTOS3 WHERE SECCION='confección'")#IMPORTANTE ESCRIBIR EL NOMBRE DE LOS CAMPOS Y DEL RESTO DE INFORMACION DE ACUERDO A COMO SE HIZO EN LA BBDD, INCLUIDOS ACENTOS, minúsculas, ETC.
productos=miCursor3.fetchall()
print(productos)



#UPDATE__________________________________________________________________________________
miCursor3.execute("UPDATE PRODUCTOS3 SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")  #si no ponemos WHERE se cambiaran todos los precios



#DELETE__________________________________________________________________________________
miCursor3.execute("DELETE FROM PRODUCTOS3 WHERE NOMBRE_ARTICULO='pantalones'") #si no ponemos WHERE se borraria toda la bbdd.


#a continuacion un commit y un close por cada una de las bbdd creadas como ejemplo

# miConexion.commit()
# miConexion.close()

miConexion2.commit()
miConexion2.close()

miConexion3.commit()
miConexion3.close()











