#COMBINACION DE MODELOS. RANDOM FOREST

#vamos a construir un modelo en el conjunto de datos de flores iris, que es un conjunto de clasificación famoso. Comprende la longitud y ancho del sépalo, longitud y áncho del pétalo y el tipo de flor. Hay 3 especies: setosa, versicolor y virginia.

#construiremos un modelo para clasificar el tipo de flor. El conjunto de datos está disponible en scilit-learn o tambien se puede descargar desde el repositorio de aprendizaje de UCI

#comenzamos importando la biblioteca de conjuntos de datos desde scikit_learn y cargamos el conjuntop de datos de iris con .load_iris()

#import scikit-learn dataset library

from ast import increment_lineno
from numpy import float64
from sklearn import datasets
#cargar datasets
iris = datasets.load_iris()

#podemos imprimir los nombres de destino y de características para asegurarnos de que tenemos el conjunto de datos correcto:

#mostrar las etiquetas de especies (setosa, versicolor, virginica)
print(iris.target_names)
#mostrar los nombres de las 4 características:
print(iris.feature_names)
#el resultado es el esperado.
#['setosa''versicolor''virginica']
#['sepal length(cm)','sepal width (cm)','petal length (cm)','petal width (cm)']
#vamos a explorar un poco los datos, para ello, mostraremos las primeras 5 filas del conjunto de datos, asi como la variable de destino para todo el conjunto de datos.
#mostrar datos iris (primeros 5 registros)
print(iris.data[0:5])
#mostrar las etiquetas iris (0: setosa, 1:versicolor, 2:virginica)
print(iris.target)
#la salida es
#[[5.1 3.5 1.4 0.2]
# [4.9 3.0 1.4 0.2]
# [4.7 3.2 1.3 0.2]
# [4.6 3.1 1.5 0.2]
# [5.0 3.6 1.4 0.2]]
# [00000.....00001111.....11112222....2222]
# a continuación vamos a crear un DataFrame del conjunto de datos de iris
import pandas as pd
data = pd.DataFrame({'sepal length':iris.data[:,0],
'sepal width':iris.data[:,1],
'petal length':iris.data[:,2],
'petal width':iris.data[:,3],
'species':iris.target})
data.head()

#en primer lugar, se separan las columnas en variables dependientes e independientes (o características y etiquetas). Luego se dividen esas variables en un conjunto de entrenamiento y prueba.

#iport train_test_split function
from sklearn.model_selection import train_test_split
X=data[['sepal length', 'sepal width', 'petal length', 'petal width']] #features
y = data['species']#labels
#dividir dataset en training set y test set
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)#70% training y 30% test

#después de dividir, se entrena el modelo con el conjunto de entrenamiento y se reallizarán predicciones en el conjunto de prueba.
#import random Forest Model
from sklearn.ensemble import RandomForestClassifier
#crear Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)
#entrenar el model utilizando training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

#después del entrenamiento, verificamos la precisión utilizando valores reales y predichos.
#importar scikit-learm metrics module para cálculo de exactitud
from sklearn import metrics
#MOdel Accuracy, ¿con que frecuencia es correcto el clasificador?
print("Exactitud:", metrics.accurancy_score(y_test, y_pred))
('Exactitud:', 0.9333333333333335)

#también es posible hacer una predicción para un sólo elemento, por ejemplo:
#longitud del sépalo=3
#ancho del sépalo = 5
#longitud del pétalo = 4
#ancho del pétalo = 2
#ahora podemos predecir que tipo de flor es
clf.predict([3,5,4,2])
#el resultado es: array([2])
#El valor 2 indica virginica

#con scikit-learn podemos encontrar características importantes. En este caso, estamos encontrando características importantes o seleccionando características en el conjunto de datos IRIS.
#En scikit-learn, puede reallizar esta tarea en los siguientes pasos:
#  - en primer lugar , creamos un modelo de bosques aleatorios
#  - en segundo lugar, utilizamos la variable de importancia de la característica para ver las puntuaciones de importancia de la característica.
#  - en tercer lugar, visualizar estas puntuaciones usando la biblioteca seaborn

from sklearn.ensemble import RandomForestClassifier
#crear Gaussian Classifier
clf = RandomForestClassifier(n_estimators=100)
#entrenar el modelo usando training sets y_pred=clf.predict(X_test)
clf.fit(X_train, y_train)
RandomForestClassifier(bootstrap=True, class_weight=None, criterior='gini', max_depth=None, max_features='auto', max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=1, oob_score=False, random_state=None, verbose=0, warm_start=False)
import pandas as pd
feature_imp = pd.Series(clf.feature_importances_,index=iris.feature_names).sort_values(ascending=False)

feature_imp
#el resultado es 
#petal width(cm) 0.458607
#petal length(cm) 0.413859
#sepal length(cm) 0.103600
#sepal width(cm) 0.023933
#dtype:float64

#también podmeos visualizar la importancia de la característica. Las visualizaciones son fáciles de entender o interpretables.
#para la visualizacion, podemos utilizar una combinación de matplotlib y seaborn. Debido a que seaborn está construido conre matplotlib, ofrece una serie de temas personalizados y proporciona tipos de trama adicionales. Matplotlib es un superconjunto de seaborn y ambos son igualmente de importantes para las buenas visualizaciones.

import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline 
#crear un bar plot
sns.barplot(x=feature_imp, y=feature_imp.index)
#añadir etiquetas al gráfico
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("visualizing important features")
plt.legend()
plt.show()

#para generar el modelo en funciones seleccionadas, podemos por ejemplo eliminar la función de "ancho de sépalo" porque tiene muy poca importancia y seleccionar las 3 características restantes.
#import train_test_split function
from sklearn.model_selection import train_test_split
#dividir dataset en features y labels
X=data[['petal length', 'petal width', 'sepal length']]#removed feature 'sepal width'
y = data['species']
#dividir dataset en training set y test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.70, random_state=5)#70% training y 30% test

#después dela división, se genera un modelo sobre las características seleccionadas del conjunto de entrenamiento, realizará predicciones sobre las características del conjunto de pruebas seleccionadas y comprobará los valores reales y previstos.
from sklearn.ensemble import RandomForestClassifier
#create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)
#entrenar el modelo usando training sets y_pred = clf.predict(X_test)
clf.fit(X_train, y_train)
#prediccion sobre test set
y_pred=clf.predict(X_test)
#importar scikit-learn metrics module para cálculo exactitud
from sklearn import metrics
#model accuracy ¿con que frecuencia es correcto el clasificador?
print("Exactitud:", metrics.accuracy_score(y_test, y_pred))
#(Exactitud:',0.95238092380...)
#podemos ver que despues de eliminar las características menos importantes (anchura de sépalo), la precisión aumentó. Esto se debe a que se eliminaron datos engañosos y ruido, lo que resultó en una mayor precisión. Una menor cantidad de características también reduce el tiempo de entrenamiento.

