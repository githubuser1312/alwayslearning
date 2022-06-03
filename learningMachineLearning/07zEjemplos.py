import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree 

iris = load_iris() #cargamos el conjunto de datos de iris
dir(iris)#con dir vemos los métodos y atributos que contiene load_iris
print(iris.feature_names) #características del dataset
print(iris.target_names)# nombres de destina en el conjunto de datos

#hay que eliminar unas etiquetas que están en la posición 0, 50 y 100 para poder entrenar mejor al árbol de decisión  y verificar si es capaz de clasificar bien los datos (utilizando los datos eliminados)

removed=[0,50,100]
new_target = np.delete(iris.target, removed) #borra las etiquetas (son los numeros 0,1,2 que represetan los tres tipos de flores) de las posiciones mencionadas
print(new_target)
new_data = np.delete(iris.data, removed, axis=0) #borra los datos de las posiciones mencionadas (se utilizaran después para verificar si funciona bien)
print(new_data)


#Para entrenar el árbol de decisión se usa un clasificador de árbol de decisión de scikit-learn para la clasificación.
#Entrenar clasificador.

clf = tree.DecisionTreeClassifier() #definir árbol de decisión clasificador
clf = clf.fit(new_data, new_target) # entrenar datos sobre new_data y new_target
prediction = clf.predict(iris.data[removed])#asignar los datos eliminados a la entrada

#ahora podemos comprobar si las etiquetas predichas coinciden con las etiquetas originales.
print('Original Labels', iris.target[removed])
print('Labels Predicted', prediction)

#el resultado muestra que la precisiòn del modelo es del 100%.
tree.plot_tree(clf) #dibujo del árbol de decisión