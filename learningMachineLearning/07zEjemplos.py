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


#EJEMPLO 1 DEL PROFESOR EN MASTERCLASS

#mostramos la tabla de datos
import pandas as pd
df = pd.DataFrame({
    'Altura': [7,7,37,37],
    'Peso': [0.6, 0.6, 0.8, 0.8],
    'Temperatura': [40,41,37,38],
    'Etiqueta': ['Gato(0)','Gato(0)', 'Perro(1)','Perro(1)']
})
df
#pasamos a vectores las caracteristicas de los animales
features = [[7,0.6,40],[7,0.6,41],[37,0.8,37],[37,0.8,38]]
labels = [0,0,1,1]
#importamos libreria 
from sklearn import tree
classifier = tree.DecisionTreeClassifier()
classifier.fit(features, labels)
#le pasamos unos valores y nos devuelve si es un gato o un perro
resultado = classifier.predict([[7,0.6,41]])
print(resultado)
#el resultado es 0, por lo tanto gato


#EJEMPLO 2 DEL PROFESOR EN MASTERCLASS

#porcentaje de personas que usan internet según la edad

#cargamos los datos
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/sotastica/data/main/uso_internet_espana.csv')
#cogemos solo una muestra
df.sample(10)

#cambiar valores de texto a 0 y 1
df = pd.get_dummies(data=df, drop_first=True)
df

#seleccionamos las variables
#variable explicativa
Explicativa = df.drop(columns='uso_internet')
#variable objetivo
Objetivo = df.uso_internet

#entrenar el modelo
#importamos libreria
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth=3)
#max_depth es para indicar los niveles del árbol de decisión que en este caso queremos sea 3
#si no indicamos cuantos niveles queremos que use, usará todos y el árbol será muy grande y necesitará mas tiempo y usará mas recursos
#probamos sin usar max_depth y vemos que el arbol tarda mucho en salir
#entrenar
model.fit(X=Explicativa, y=Objetivo)

#visualizar el modelo que tenemos entrenando
from sklearn.tree import plot_tree
#la siguiente linea tarda bastante en ejecutarse si no usamos max_depth como hemos comentado arriba
# 
# NOTA: ES IMPORTANTE EL PUNTO Y COMO DEL FINAL DE LA LÍNEA PARA QUE SE REPRESENTE CORRECTAMENTE EL ARBOL DE DECISIONES

plot_tree(decision_tree=model,feature_names=Explicativa.columns, filled=True);
#como se ve muy pequeño vamos a cambiar a matplotlib
import matplotlib.pyplot as plt
plt.figure(figsize=(20,15))
plot_tree(decision_tree=model,feature_names=Explicativa.columns, filled=True, fontsize=12);
#cogemos una muestra y ,visualmente, seguimos la logica del arbol (si es a la izda y no a la derecha)
muestra = Explicativa.sample()
print(muestra)
#porcentajes de personas que usan y no usan internet en el grupo de edad de la persona de 'muestra'
model.predict_proba(muestra)

