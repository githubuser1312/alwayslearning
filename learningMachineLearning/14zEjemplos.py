# MANIFOLD

#Veamos una ilustración de la reduccion de dimensionalidad en el conjunto de datos de la curva S con varios métodos.

# Hay que tener en cuenta que el propósito del MDS es encontrar una representación de baja dimensión de los datos (en este caso 2D) en la que las distancias respeten bien la distancias en el espacio original de alta dimensión, a diferencia de otros algoritmos de aprendizaje múltiple, no busca una representación isotrópica de los datos en el espcio de baja dimensión.

from collections import OrderedDict
from functools import partial
from time import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
from sklearn import manifold, datasets

Axes3D
n_points = 1000
X, color = datasets.make_s_curve(n_points, random_state=0)
n_neighbors = 10
n_components = 2

#Create figure
fig = plt.figure(figsize=(15,8))
fig.suptitle("Manifold Learning con %i puntos, %i vecinos" % (1000, n_neighbors), fontsize =14)

#3D scatter plot
ax = fig.add_subplot(251, projection="3d")
ax.scatter(X[:,0],X[:,1],X[:,2], c=color, cmap=plt.cm.Spectral)
ax.view_init(4,-72)

#Configurar métodos manifold
LLE = partial( manifold.LocallyLinearEmbedding, n_neighbors=n_neighbors, n_components=n_components, eigen_solver="auto")
methods =OrderedDict()
methods["LLE"]=LLE(method="standard")
methods["LTSA"]=LLE(method="ltsa")
methods["Hessian LLE"]=LLE(method="hessian")
methods["Modified LLE"]=LLE(method="modified")
methods["Isomap"]=manifold.Isomap(n_neighbors=n_neighbors, n_components=n_components)
methods["MDS"]=manifold.MDS(n_components, max_iter=100, n_init=1)
methods["SE"]=manifold.SpectralEmbedding(n_components=n_components, n_neighbors=n_neighbors)
methods["t-SNE"]=manifold.TSNE(n_components=n_components, init="pca", random_state=0)

#dibujar resultados
for i , (label, method) in enumerate(methods.items()):
    t0 = time()
    Y = method.fit_transform(X)
    t1 = time()
    print("%s: %.2g sec" % (label, t1 - t0))
    ax = fig.add_subplot(2,5,2+i+(i>3))
    ax.scatter(Y[:,0],Y[:,1], c=color, cmap=plt.cm.Spectral)
    ax.set_title("%s(%.2g sec)" % (label, t1-t0))
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    ax.axis("tight")
    plt.show()