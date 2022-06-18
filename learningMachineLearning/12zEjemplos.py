#El algoritmo Biclustering consta de 5 pasos:

# 1- Bistocaización: una fase iterativa de preprocesamiento donde los valores de aij se ajustan para que todas las sumas de filas y columnas sumen un valor común constante (generalmente 1).

# 2- Descomposiición de la matriz bistocástica A pertenece a R nxm. Los valores singulares se ordenan en orden descendente y los vectores singulares se reorganiczan en consecuencia.

# 3- Ranking de los vectores singulares analizando su similitud con la estructura del tablero de ajedrez se resaltará con biclustering.

# 4- Proyección el conjunto de datos en el subespacio abarcado por las columnas de aij

# 5- Aplicación de K-Means para encontrar el etiquetado delkracimos. Esta operación produce dos vectores de etiquetas,

#NOTA: la info anterior que me da el curso no está nada clara, buscar en internet. (además usan imagenes borrosas)

# Para implementar biclustering espectral, primero necesitamos un conjunto de datos. Por razones prácticas, podemos generar un conjunto de datos artificiales que consta de: 199 usuarios, 100 transacciones(compras), 100 productos, clasificaciones en el rango 1-10 (10 posibles biclusters diferentes).

import numpy as np
nb_users = 100
nb_products = 100
items = [i for i in range(nb_products)]
transactions = []
ratings = np.zeros(shape=(nb_users, nb_products), dtype=np.int)
for i in range(nb_users):
    n_items = np.random.randint(2,60)
    transaction = tuple(np.random.choice(items, replace=False, size=n_items))
    transactions.append(list(map(lambda x: "P{}".format(x+1), transaction)))
for t in transaction:
    rating = np.random.radint(1,11)
    rating[i,t] = rating

#ppodemos visualizar las calificaciones generadas en un mapa de calor:

import seaborn as sns

sns.heatmap(ratings, center=0)

#Ahora podemos implementar el algoritmo de biclustering espectra con scikit learn:

from sklearn.cluster import SpectralBiclustering

sbc = SpectralBiclustering(n_clusters =10, n_best = 5, #proyectar el data set en el top5 de vectores singualres
svd_method = "arpack", #bueno para matrices medianas pequeñas
n_jobs = -1,
random_state=1000)

sbc.fit(ratings)

#A continuación, necesitamos calcular la matriz final utilizando el producto externo de los indices de fila y columna ordenados:

rc = np.outer(np.sort(sbc.row_labels_)+1,
np.sort(sbc.column_labels_)+1)

#También podemos visualizar la matriz reorganizada en un mapa de calor:

sns.heatmap(rc)

#Finalmente, podemos usar la matriz para un caso de uso práctico de marketing: determinar el grupo de usuariios que calificaron un grupo de cinco productos para enviar a esos usuarios un boletín con recomendaciones de productos. Para hacer eso necesitamos seleccionar todas las filas y columnas asociadas con los clusteres con un índice de 5 ( porque 0 significa sin calificación).

print("Usuarios: {}".format(np.where(sbc.rows_[8,:] == True)))
print("Productos: {}".format(np.where(sbc.columns_[8,:] == True)))

#el resultado que arroja lo anterior significa que debemos verificar los productos en del array Productos, seleccionar otros propductos que sean similares a esos y enviarlos a los usuarios del array Usuarios.

#NOTA: DA ERROR NO FUNCIONA!!!!!!!!!!!