###############     METODO K-MEANS
''' usaremos scikit-learn para K-means clustering'''
''' partimos de un conjunto de 10 puntos de datos'''

'''    Object       X_value     Y_value
    Object1         1.005079    4.594642
    Object2         1.128478    4.328122
    Object3         2.117881    0.726845
    Object4         0.955626    4.385907
    Object5         -1.35402    2.769449
    Object6         -1.07295    2.627009    
    Object7         -2.03750    3.048606
    Object8         2.354083    0.856632
    Object9         2.144040    0.964399
    Object10        1.166288    4.273516
'''

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
from sympy import N

X = pd.DataFrame({'X-values':[1.005079, 1.128478, 2.117881, 0.955626, -1.35402, -1.07295, -2.0375, 2.354083, 2.14404, 1.166288],
                 'Y-values': [4.594642, 4.328122, 0.726845, 4.385907, 2.769449, 2.627009, 3.048606, 0.856632, 0.964399, 4.273516]})

#especificar el numero de clusters (3) y fit datos X para entrenar el modelo

kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

#extraigamos los centroides de cluster y las etiquetas de clúster de la variable K-Means

print(kmeans.cluster_centers_)
print(kmeans.labels_) #el resultado que se ve aqui es una matriz de una columna con 3 valores 0,1 y 2. Cada valor corresponde a un grupo y a ese grupo pertenece cada pareja de valores X-value, Y-value. Por ejemplo el print puede ser [2212000112] porque el primer, y segundo par de valores se etiquetan con el mismo nombre que es 2. El tercer par de valores se etiqueta con el nombre 1, el cuarto par se etiqueta con el nombre 2 porque es del mismo cluster que los dos primeros, etc.

#tracemos los centroides del cluster con respecto a los puntos de datos, para tener una representacion gráfica

plt.scatter(X.iloc[:,0],X.iloc[:,-1])
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], c='red', marker='x')
plt.title('Puntos de datos y centroides')
plt.show()



###################        METODO DBSCAN

''' Para generar el conjunto de datos haremos dos cosas:
1- especificar algunas opciones de configuracion y las usaremos en la llamada
2- usaremos make-blobspsilonmin_samples'''

from sklearn.datasets import make_blobs #conjunto de datos basados en blobs
from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt

#configuracion
num_samples_total = 1000
cluster_centers = [(3,3),(7,7)]
num_classes = len(cluster_centers)
epsilon = 0.3
min_samples = 13
#generar datos
X,y = make_blobs(n_samples = num_samples_total, centers=cluster_centers, n_features = num_classes, center_box=(0,1), cluster_std = 0.5)

#los datos se generan al azar asi que serán ligeramante diferentes cada vez que ejecutemos.

#para poder repetir el proceso, puede ser aconsejable guardar los datos solo una vez después de ejecutar el script: al quitar los comentarios de la línea (np.save...), siempre cargará los mismos datos del archivo. Sin embargo, esto no es necesario.
#grabar datos si se considera necesario

#np.save('learningMachineLearning/11zClusters.npy', X)
#X = np.load('learningMachineLearning/11zClusters.npy')

#ahora podemos inicializar DBSCAN y calcular los clusteres

# inicializamos con nuestros valores con DBSCANepsilonmin_samples.
# luego ajustamos inmediatamente los datos a DBSCAN, lo que significa que comenzará la agrupacion en clusteres
#cargamos las etiquetas generadas (es decir, índices de cluster) una vez finalizado el agrupamiento.

db = DBSCAN(eps=epsilon, min_samples=min_samples).fit(X)

labels = db.labels_

no_clusters = len(np.unique(labels))
no_noise = np.sum(np.array(labels) == -1, axis = 0)

print('Estimación no. clusters: %d' % no_clusters)
print('Estimacion no. noise points: %d' % no_noise)

#podemos generar un diagrama de dispersion para nuestros datos de entrenamiento. Dado que tenemos dos clústeres, utilizamos una función lambda simple que slecciona un color u otro. Si tenemos varios clusteres, podemos generalizar fácilmente esta función lambda con un enfoque diccionario.

colors = list(map(lambda x: '#3b4cc0' if x == 1 else '#b40426', labels))

plt.scatter(X[:,0], X[:,1], c=colors, marker = "o", picker = True)

plt.title('Dos clusteres con datos')
plt.xlabel('Eje X[0]')
plt.ylabel('Eje X[1]')
plt.show()

#si adaptamos el valor de epsilon y lo establecemos en 0.3 obtenemos diferentes resultados. En concreto, el algoritmo es ahora capaz de detectar muestras ruidosas, como podemos ver en la imagen que se obtiene al usar ese epsilon. Sin embargo, eliminar las muestras ruidosas después de realizar DBSCAN es fácl y requiere sólo 4 líneas de código. Esto se debe a que DBSCAN establece las etiquetas para muestras con ruido en ; esta es su forma de señalar una etiqueta como ruidosa.-1 (las lineas de código hay que agregarlas antes de generar el diagrama).

#quitar ruido

range_max = len(X)

X = np.arrray([X[i] for i in range(0, range_max) if labels[i]!= -1])

labels = np.array (labels[i] for i in range(0,range_max) if labels[i] != -1)

#dibujar scatter plot para datos de entrenamiento
colors = list(map(lambda x: '#000000' if x == -1 else '#b40426', labels))

plt.scatter(X[:,0], X[:,1], c = colors, marker="o", picker=True)

plt.title('Ruido quitado')
plt.xlabel('Eje X[0]')
plt.ylabel('Eje X[1]')
plt.show()



###################        METODO MEZCLA GAUSSIANA

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture
import numpy as np

sns.set_context("talk", font_scale=1.5)

#usaremos la funcion de make_blobs de sklearn.datasets para crear un conjunto de datos simulado con 4 clusteres diferentes. El argumento centers=4 especifica 4 clusteres. Tambien especificamos cómo de apretado debe ser el clúster usando cluster_std.

X,y = make_blobs(n_samples = 500, centers=4, cluster_std=2, random_state=2021)

#la funcion make_blobs nos da los datos simulados como una matriz numpy y las etiquetas como vector.Almacenemos los datos como dataframe de Pandas.

data = pd.DataFrame(X)

data.columns = ["X1","X2"]
data["cluster"]=y
data.head()

#con la funcion GaussianMix() de scikit learn, podemos ajustar nuestros datos a los modelos de mezcla. Uno de los parámetros clave a usar al ajustar el modelo de mezcla gaussiana es el número de clústeres en el conjunto de datos.

#Para este ejemplo, construyamos el modelo de mezcla gaussiana con 3 clusteres. Dado que simulamos los datos con 4 clusteres, sabemos que es incorrecto, pero sigamos adelante y ajustemos los datos con el modelo de mezcla gaussiana.

gmm = GaussianMixture(3,covariance_type='full', random_state=0).fit(data[["X1","X2"]])

#para los clusteres identificados, podemos obtener la ubicación de los medios utilizando el método "means_" en GaussianMixture.

gmm.means_


#usando la función predict(), también podemos predecir las etiquetas para los puntos de datos. En este ejemplo, obtenemmos los valores predichos para los datos de entrada.

labels = gmm.predict(data[["X1","X2"]])

#agregemos las etiquetas predichas a nuestro marco de datos.

data["predicted_cluster"] = labels

#Finalmente visualizamos los datos coloreando los puntos de datos con etiquetas predichas.

plt.figure(figsize=(9,7))

sns.scatterplot(data=data, x="X1", y="X2", hue="predicted_cluster", palette = ["red", "blue", "green"])

plt.savefig("fitting_Gaussian_Mixture_models_with_3_components_scikit_learn_Python.png", format='png', dpi=150)

#podemos ver claramente que al ajustar el modelo con 3 clusteres es incorrecto. El modelo ha agrupado dos clústeres en uno.

#A menudo el mayor desafío es que nos sabremos los grupos de números en el conjunto de datos. Necesitamos identificar correctamente el número de grupos. Una de las formas en que podemos hacerlo es ajustar el modelo de mezcla gaussiana con un número múltiple de grupos, digamos que van de 1 a 20.
#y luego hacemos una comparación de modelos para encontrar que modelo se ajusta primero a los datos. Por ejemplo, es un modelo de mezcla gaussiana con 4 clusteres que encajan mmejor o un modelo con 3 clústeres que encajen mejor. Después podemos seleccionar el mejor modelo con cierto número de clústeres que se ajuste a los datos.

#Las puntuaciones AIC o BIC se usan habitualmente para comparar modelos y seleccionar el mejor modelo que se ajuste a los datos. Una sola de las puntuaciones es lo suficientemente buena como para hacer una comparación de modelos. Sin embargo vamos a calcular ambas puntuaciones, sólo para ver su comportamiento.

#ajustamos los datos con el modelo de mezcla gaussiana con diferentes números de grupos.

n_components = np.arange(1,21)

models = [GaussianMixture(n, covariance_type='full', random_state=0).fit(X) for n in n_components]
models[0:5]
[GaussianMixture(random_state=0), GaussianMixture(n_components=2, random_state=0), GaussianMixture(n_components=3, random_state=0), GaussianMixture(n_components=4, random_state=0), GaussianMixture(n_components=5, random_state=0)]

#podemos clacular facilmente los puntajes AIC / BIC con scikit_learn. Aqui usamos para uno de los modelos y calculamos las puntuaciones BIC y AIC

models[0].bic(X)
models[0].aic(X)

#Para comprobar cómo cambia la puntuación BIC/AIC con respecto al número de componentes usados para construir el modelo de mezcla gaussiana, vamos a crear una tabla de datos que contenga las puntuaciones BIC y AIC y el numero de componentes

gmm_model_comparisons = pd.DataFrame({"n_componentes": n_components, "BIC": [m.bic(X)for m in models], "AIC":[m.aic(X) for m in models]})

gmm_model_comparisons.head()

#Ahora podemos hacer una gráfica de línea de AIC/BIC frente a los componentes numéricos.

plt.figure(figsize=(8,6))
sns.lineplot(data=gmm_model_comparisons[["BIC","AIC"]])
plt.xlabel("Numero de clusteres")
plt.ylabel("Puntuación")
plt.savefig("GMM_model_comparison_with_AIC_BIC_Scores_python.png", format='png', dpi=150)


#podemos ver que la puntuación BIC y AIC están en el nivel más bajo cuando el número de componentes es 4. Por lo tanto, el modelo con n=4 es el mejor modelo.

###################        METODO BIRCH

from sklearn.cluster import Birch
import numpy as np
import matplotlib.pyplot as plt

#preparamos datos, creando datos aleatorios de agrupacion en clústeres simples.

np.random.seed(12)
p1 = np.random.randint(5,21,110)
p2 = np.random.randint(20,30,120)
p3 = np.random.randint(8,21,90)
data = np.array(np.concatenate([p1,p2,p3]))
x_range = range(len(data))
x = np.array(list(zip(x_range, data))).reshape(len(x_range),2)
print(x)

#mostramos los datos
plt.scatter(x[:,0],x[:,1])
plt.show()

#definimos el método BIRCH y lo ajustamos con x datos. Establecemos parámetros de branching_factor y parámetros de umbral (threshold). El branching_factor define el número de subgrupos y el umbral establece el límite entre la muestra y el subgrupo.

bclust = Birch(branching_factor = 100, threshold = 0.5).fit(x)

print(bclust)

Birch(branching_factor = 100, compute_labels=True, copy=True, n_clusters=3, threshold=0.5)

#el método identifica el número de clústeres que se van a asiggnar. También se puede configurar manualemente. Ahora, podemos predecir x datos para obtener el id de clústeres de destino.

labels = bclust.predict(x)

#finalmente verificamos los puntos agrupados en una gráfica separándolos con diferentes colores.

plt.scatter(x[:,0],x[:,1],c=labels)
plt.show()


###################        METODO AFFINITY PROPAGATION

from sklearn.cluster import AffinityPropagation
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

#a continuación añadimos algunas opciones de configuración: el número de muestras en total que generamos, los centros de los clústeres, así como el número de clases para las que generamos muestras. Todos ellos se utilizarán en make_blobs, que genera los clusteres y los asigna X y targets, respectivamente.
#Los guardamos con Numpy y posteriormente los cargamos y asignamos a X de nuevo. Esas dos líneas de código no son necesarias para que el modelo se ejecute, pero si deseamos comparar entre configuraciones, es probable que no deseemos generar muestras al azar cada vez. Al guardarlos una vez, y posteriormente comentar las instrucciones sabe y make_blobs se cargarán desde el archivo.

#opciones de configuración:
num_samples_total = 50
cluster_centers = [(20,20),(4,4)]
num_classes = len(cluster_centers)

#generar datos
X, targets = make_blobs(n_samples = num_samples_total, centers = cluster_centers, n_features = num_classes, center_box=(0,1), cluster_std = 1)


#np.save('learningMachineLearning/11zClustersAffinityPropagation.npy', X)
#X = np.load('learningMachineLearning/11zClustersAffinityPropagation.npy')


#ajustamos los datos al algoritmo de propagacion de afinidad, después de cargarlo, que solo necesita dos líneas de código. En otras lineas, derivamos características como los ejemplares y en consecuencia el número de clusters.

#Fit affinity propagation with Scikit

afprop= AffinityPropagation(max_iter=250)
afprop.fit(X)
cluster_centers_indices = afprop.cluster_centers_indices_
n_clusters_ = len(cluster_centers_indices)

#finalmente mediante el algoritmo que encajamos, predecimos para todas nuestras muestras a que cluster pertenecen:

#predecir al cluster para todas las muestras
P = afprop.predict(X)
 
#y finalmente visualizar el resultado, general scatter plt para training data
colors = list(map(lambda x:'#3b4cc0' if x == 1 else '#b40426', P))
plt.scatter(X[:,0], X[:,1], c = colors, marker ="o", picker = True)
plt.title(f'Numero estimado de clusteres = {n_clusters_}')
plt.xlabel('Temperatura ayer')
plt.ylabel('Temperatura hoy')
plt.show()





###################        METODO MEAN-SHIFT CLUSTERING

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import MeanShift, estimate_bandwidth

#usaremos matplotlib para generar visualizaciones, numpy para algun procesamiento de números y la funcionalidad Scikit-learn para generar el conjunto de datos (es decir, los blobs de datos no agrupados) y la operacion de agrupacion en clústeres real.
#Una vez definidas las importaciones, podemos establecer las opciones de configuración:

#configuración

num_samples_total = 10000
cluster_centers = [(5,5), (3,3), (1,1)]
num_classes = len(cluster_centers)

#general datos
X,targets = make_blobs(n_samples = num_samples_total, centers = cluster_centers, n_features = num_classes, center_box = (0,1), cluster_std = 0.30)

#podemos hacer que Scikit-learn genere los blobs que queramos, establecemos la configuración que acabamos de definir y establecemos una desviación estándar del clúster de 0,30. Esto puede ser casi cualquier cosa, es posoible jugar con este valor para ver distintos resultados

#es posible que desee guardar el conjunto de datos generados y trabajar siempre con los mismos datos, con las siguientes líneas:

np.save('learningMachineLearning/11zClustersMeanShiftClustering.npy', X)
X = np.load('learningMachineLearning/11zClustersMeanShiftClustering.npy')

#a continuación , llegaremos a la funcionalidad específica de Mean Shift. Primero, definimos lo que se conoce como el "ancho de banda" del algoritmo, como se puede ver aqui:

#bandwith estimado

bandwidth = estimate_bandwidth(X, quantile = 0.2, n_samples = 500)

#Mean Shift mira a su alrededor y determina la dirección a la que debe moverse una muestra, es decir, donde probablemente esté el centroide del cluster. Sin embargo, sería demasiado costoso computacionalmente hacerlo para todas las muestras, porque entonces el algoritmo se atascaría.
#es por eso que el "ancho de banda" ayuda: simplemente define un área alrededor de las muestras donde mirar el cambio medio para determinar la ruta más probable dada la estimación de densidad. Pero, ¿cuál debería ser este valor de ancho de banda? Ahí es donde entra en juego, y estima el ancho de banda m´sa adecuado en función del dataset.estimate_bandwidth

#Inmediatamente usamos el ancho de bando en la instanciacion de algoritmo Mean Shift, después de lo cual ajustamos los datos y generamos algunos datos consecuentes, como el número de etiquetas:

#fit Mean Shift con Scikit

meanshift = MeanShift(bandwidth=bandwidth)
meanshift.fit(X)
labels = meanshift.labels_
labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)

#Luego, generamos predicciones para todas las muestras de nuestro conjunto de datos.

P = meanshift.predict(X)

#finalmente generamos una visualizacion para ver si nuestra operación de clustering es exitosa.

colors = list(map(lambda x: '#3b4cc0' if x == 1 else '#b40426' if x == 2 else '#67c614', P))

plt.scatter(X[:,0], X[:,1], c=colors, marker="o", picker=True)
plt.title(f'Numero estimado de clusteres = {n_clusters_}')
plt.xlabel('Temperatura ayer')
plt.ylabel('Temperatura hoy')
plt.show()

#IMPORTANTE: EL CODIGO TARDA UN PAR DE MINUTOS EN EJECUTARSE.






###################        METODO OPTICS

#Con el siguiente código podemos realizar clustering basado en OPTICS en un conjunto de datos aleatorio similar a un blob. Funciona de la siguiente manera:

# 1- Hacemos todas las importaciones para generar los datos, para la agrupacion en clusteres y Numpy y Matplotlib para el procesamiento y la visualizacion.
# 2- Especificamos una gama de opciones de configuración. Generamos 1000 muestras en total alrededor de dos centros, de modo que obtendremos dos blobs de datos. Establecimos epsilon y min_smaples a valores que derivamos durante las pruebas, así como el método para agrupar y la métrica de distancia.
# 3- La distancia de Minkowski es la métrica predeterminada
# 4- A continuación generamos datos: dos blobs de datos, con .make_blobs
# 5- En vase a estos datos, realizamos clustering basado en OPTICS, con epsilon, número mínimo de muestras, método de cluster y métrica definida. Inmediatamente ajustamos los datos para que se generen los clusteres.
# 6- Luego imprimimos información sobre el úmero de clusteres y muestras ruidosas y finalmente generamos un diagrama de dispersion.

from sklearn.datasets import make_blobs
from sklearn.cluster import OPTICS
import numpy as np
import matplotlib.pyplot as plt

#configuración
num_samples_total = 1000
cluster_centers = [(3,3),(7,7)]
num_classes = len(cluster_centers)
epsilon = 2.0
min_samples = 22
cluster_method = 'xi'
metric = 'minkowski'
#generar datos
X,y = make_blobs(n_samples = num_samples_total, centers = cluster_centers, n_features = num_classes, center_box=(0,1), cluster_std = 0.5)
#computar OPTICS
db = OPTICS(max_eps = epsilon, min_samples = min_samples, cluster_method = cluster_method, metric = metric).fit(X)

labels = db.labels_
no_clusters = len(np.unique(labels))
no_noise = np.sum(np.array(labels) == -1, axis=0)
print('Estimado nº clusters: %d' % no_clusters)
print('Estimado nº noise points: %d' % no_noise)

#generar scatter plot para training data

colors = list(map(lambda x: '#3b4cc0' if x == 1 else '#b40426', labels))
plt.scatter(X[:,0], X[:,1], c=colors, marker='o', picker=True)
plt.title('OPTICS clustering')
plt.xlabel('Axis X[0]')
plt.ylabel('Axis X[1]')
plt.show()

#tambien podemos generar la grafica de accesibilidad
reachability = db.reachability_[db.ordering_]
plt.plot(reachability)
plt.title('Reachability plot')
plt.show()



###################        METODO AGGLOMERATIVE HIERARCHY CLUSTERING

#los pasos para realizar el algorimto son:

# 1- tratar cada punto de datos como un solo cluster. Por lo tanto, tendremos, K grupos al principio. El número de puntos de datos también será K al principio.

# 2- necesitamos formar un gran cluster uniendo dos puntos de datos de armario. Esto dará como resultado un total de clusteres K-1

# 3- para formar más clusteres necesitamos unir los dos puntos más cercanos. Esto dará como resultado un total de clusteres K-2

# 4- para fomar un gran cluster, repetimos los tres pasos anteriores hasta que K se convierta en 0, es decir, no queden más puntos de datos para unirse

# 5- por último, después de hacer un sólo clúster grande, se utilizarán dendogramas para dividir en múltiples grupos dependiendo del problema.

# %matplotlib inline (esta es la primera linea en el ejemplo del curso, pero aqui no funciona, es una linea de IPython).

import matplotlib.pyplot as plt
import numpy as np

#a continuación trazaremos los puntos de datos que hemos tomado para este ejemplo.

X = np.array([[7,8],[12,20],[17,19],[26,15],[32,37],[87,75],[73,85],[62,80],[73,60],[87,96]])

labels = range(1,11)
plt.figure(figsize=(10,7))
plt.subplots_adjust(bottom=0.1)
plt.scatter(X[:,0],X[:,1], label='True Position')
for label, x, y in zip(labels, X[:,0],X[:,1]):
    plt.annotate(label,xy=(x,y), xytext=(-3,3), textcoords='offset points', ha='right', va='bottom')
    plt.show()


# A partir del diagrama anterior, es muy fácil ver que tenemos dos clusteres en nuestros puntos de datos, pero en los datos del mundo real, puede haber miles de clusteres. A continuación, trazaremos los dendogramas de nuestros puntos de datos utilizando la biblioteca Scipy

from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
linked = linkage(X, 'single')
labelList = range(1,11)
plt.figure(figsize=(10,7))
dendrogram(linked, orientation='top', labels=labelList, distance_sort='descending', show_leaf_counts=True)
plt.show()

#Ahora que una vez que se forma el gran cúmulo, se selecciona la distancia vertical más larga. A continuación, se dibuja una línea horizontal a través de ella. Como la línea horizontal cruza la linea azul en dos puntos, el número de grupos seria de dos.
# A continuación, debemos importar la clase para la agrupación en clusteres y llamar a su método fit_predict para predecir el cluster. Estamos importando la clase AgglomerativeClustering de la biblioteca sklearn.cluster.

from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
cluster.fit_predict(X)
#a continuación trazamos el cluster
plt.scatter(X[:,0],X[:,1], c=cluster.labels_, cmap='rainbow')




#EJEMPLO DEL PROFESOR EN LA MASTERCLASS
from pandas import DataFrame
Data = {'x': [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
        'y':[79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]}

df = DataFrame(Data,columns=['x','y'])
df
#visualizamos en el grafico de dispersion
import matplotlib.pyplot as plt
plt.scatter(df['x'],df['y'])
plt.show()
from sklearn.cluster import KMeans
Buscando_Centroides = KMeans(n_clusters=3).fit(df)
centroids = Buscando_Centroides.cluster_centers_
#mostramos valores que se ha generado
print(centroids)
#poner los grupos en el gráfico
plt.scatter(df['x'],df['y'], c=Buscando_Centroides.labels_.astype(float),s=50, alpha=0.8)
#añadimos los centroides
plt.scatter(centroids[:,0],centroids[:,1], c='red', s=50)
plt.show()