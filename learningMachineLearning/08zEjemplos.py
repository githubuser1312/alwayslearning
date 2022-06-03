'''1) importamos bibliotecas:'''
import numpy as np 
import matplotlib.pyplot as plt
from pyrsistent import T 
from scipy import stats 
import seaborn as sns; sns.set()
'''2) creamos un conjunto de datos de muestra, que tiene datos linealmente separables, a apartir de skjlearn.dataset.sample_generator para su clasificación utilizandop SVM.'''
from sklearn.datasets import make_blobs
X,y = make_blobs(n_samples=100, centers=2, random_state=0, cluster_std=0.50)
plt.scatter(X[:,0],X[:,1],c=y, s=50, cmap='summer')
'''3) Sabemos que SVM soporta la clasificación discriminativa , divide las clases entre sí simplemente encontrando una línea en caso de dos dimensiones o una variedad en caso de múltiples dimensiones. Para implementarla en el conjunto de datos anterior lo hacemos así:'''
xfit = np.linspace(-1,3.5)
plt.scatter(X[:,0], X[:,1], c=y, s=50, cmap='summer')
plt.plot([0.6],[2.1],'x', color='black', markeredgewidth=4, markersize=12)
for m, b in [(1,0.65),(0.5,1.6),(-0.2,2.9)]:
    plt.plot(xfit, m * xfit + b, '-k')
    plt.xlim(-1,3.5)

'''(se veria el resultado en una gráfica con tres separadores que discriminan las muestras)'''
'''4) El objetivo principal de SVM es dividir los conjuntos de datos en clases para encontrar un hiperplano marginal máximo (MMH), por lo tanto, en lugar de dibujar una linea cero entre las clases, podemos dibujar alrededros de cada línea un margen de cierto ancho hasta el punto más cercano. Se puede hacer de la siguiente forma:'''
xfit = np.linspace(-1,3.5)
plt.scatter(X[:,0], X[:,1], c=y, s=50, cmap='summer')
for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]:
    yfit = m * xfit + b 
    plt.plot(xfit, yfit, '-k')
    plt.fill_between(xfit, yfit - d, yfit + d, edgecolor='none', color='#AAAAAA', alpha=0.4)
    plt.xlim(-1,3.5)
'''En la gráfica que sale podríamos ver los márgenes dentro de los clasificadores discriminativos (si no aparece usar jupyter-notebook). SVM elegirá la línea que maximice el margen.'''




'''Otro ejemplo en el que usaremos el clasificador de vectores de soporte (SVC) de Scikit-Learn para entrenar un modelo SVM sobre estos datos. Aquí, utilizaremos el kernel lineal para ajustarse a SVM de la siguiente forma:'''

from sklearn.svm import SVC 
model = SVC(kernel='linear', C=1E10)
model.fit(X,y)

''' El resultado es:
SVC(C=100000000000.0, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape='ovr', degree=3, gamma='auto_deprecated', kernel='linear',max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False'''
''' Ahora para entender mejor el proceso, definimos una función de decisión para 2D SVC:'''
def decision_function(model, ax=None, plot_support=True):
    if ax is None:
        ax=plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
'''para evaluar el modelo tenemos que crear una cuadrícula de la siguiente forma'''
    x = np.linspace(xlim[0],ylim[1],30)
    y = np.linspace(ylim[0],ylim[1],30)
    Y,X = np.meshgrid(y,x)
    xy=np.vstack([X.ravel(), Y.ravel()]).T
    P=model.decision_function(xy).reshape(X.shape)
    '''a continuación debemos trazar los límites y márgenes de decisión de la siguiente manera'''
    ax.contour(X,Y,P,colors='k', levels=[-1,0,1], alpha=0.5, linestyles=['--','-','--'])
    '''ahora , de manera similar, trazamos los vectores de soporte:'''
    if plot_support:
        ax.scatter(model.support_vectors_[:,0], model.support_vectors_[:,1], s=300, linewidth=1, facecolors='none')
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
    '''ahora usamos la función para adaptarse a nuestro modelo:'''
    plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap='summer')

decision_function(model)

'''podemos observar en la salida anterior que un clasificador SVM se ajusta a los datos con márgner, es decir,líneas discontínuas y vectores soporte, los elementos fundamentales de este ajuste, tocando la línea discontínua. Estos puntos vectoriales de soporte se almacenan en el atributo support_vectors_ del clasificador de la siguiente manera:'''

model.support_vectors_

'''el resultado es: 
        array([[0.5323772, 3.31338909], [2.11114739, 3.57660449], [1.46870582, 1.86947425]])'''
''' el código completo es el siguiente:'''
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats
import seaborn as sns; sns.set()
'''crear dataset'''
from sklearn.datasets import make_blobs

X,y = make_blobs(n_samples=100, centers=2, random_state=0, cluster_stad=0.50)
plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap='summer')
'''incluir separadores'''

xfit = np.lispace(-1,3.5)
plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap='summer')
plt.plot([0.6],[2.1],'x',color='black',markeredgewidth=4, makersize=12)
for m, b in [(1,0.65), (0.5,1.6),(-0.2,2.9)]:
    plt.plot(xfit, m * xfit + b, '-k')
    plt.xlim(-1,3.5)
'''dar margen a los separadores'''
xfit = np.linspace(-1,3,5)
plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap='summer')
for m,b,d in [(1,0.65,0.33), (0.5,1.6,0.55),(-0.2,2.9,0.2)]:
    yfit = m * xfit + b
    plt.plot(xfit, yfit, '-k')
    plt.fill_between(xfit, yfit -d, yfit + d, edgecolor='none', color='#AAAAAA', alpha=0.4)
    plt.xlim(-1,3.5)
'''utilizar SVC'''
from sklearn.svm import SVC
model = SVC(kernel='linear', C=1E10)
model.fit(X,y)
'''2D SVC'''
def decision_function(model, ax=None, plot_support=True):
    if ax is None:
        ax=plt.gca()
    xlim=ax.get_xlim()
    ylim=ax.get_ylim()
    '''crear cuadricula'''
    x=np.linspace(xlim[0],xlim[1],30)
    y=np.linspace(ylim[0],ylim[1],30)
Y,X = np.meshgrid(y,x)
xy = np.vstack([X.ravel(), Y.ravel()]).T
P = model.decision_function(xy).reshape(X.shape)
'''Dibujar límites y márgenes'''
ax.contour(X,Y,P, colors='k', levels=[-1,0,1], alpha=0.5, linestayles=['--','-','--'])
'''dibujar SVC'''
if plot_support:
    ax.scatter(model.support_vectors_[:,0], model.support_vectors_[:,1], s=300, linewidth=1, facecolors='none')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
'''dibujar resultado'''
plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap='summer')
decision_function(model)
'''mostrar vectores de soporte'''
model.support_vectors_