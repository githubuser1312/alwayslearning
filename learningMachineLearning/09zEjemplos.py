# EJEMPLO DE PERCEPTRON

#vamos a desarrollar un algoritmo que clasifique los vlaores en dos categorías: p1 y p2

#lo primero que haremos será crear una clase llamada "Perceptron", para defnir los atributos del Perceptron:
# Datos de entrenamiento
# Salida esperada
# Otras características
import cmath
import random
from re import X

class Perceptron:
    def __init__(self, sample, exit, learn_rate=0.01, epoch_number=1000, bias=-1):
        self.sample=sample
        self.exit = exit
        self.learn_rate = learn_rate
        self.epoch_number = epoch_number
        self.bias = bias
        self.number_sample=len(sample)
        self.col_sample = len (sample[0])
        self.weight = []
    #declaramos un métod dentro de la clase Perceptron llamada training para entrenar a la neurona.
    def training(self):
        for sample in self.sample:
            sample.insert(0,self.bias)
        for i in range(self.col_sample):
            self.weight.append(random.random())
            self.weight.insert(0,self.bias)
            epoch_count =0
            while True:
                erro = False
        for i in range(self.number_sample):
            u = 0
        for j in range(self.col_sample + 1):
            u = u + self.weight[j]*self.sample[i][j]
            y = self.sign(u)
            if y != self.exit[1]:
                for j in range(self.col_sample + 1):
                    self.weight[j] = self.weight[j]+self.learn_rate*(self.exit[i]-y)*self.sample[i][j]
                    erro =True
                    epoch_count = epoch_count + 1
                    if erro == False:
                        print(('\nEpoch:\n', epoch_count))
                        print('----------------\n')
                        break
        #el método sort recibe como argumentos los datos que la neurona utilizará para su entrenamiento, este método clasificará los nuevos datos con repecto a sus conocimientos.
        def sort(self,sample):
            sample.insert(0, self.bias)
            u=0
            for i in range(self.col_sample+1):
                u = u + self.weight[i]*sample[i]
                y = self.sign(u)
                if y == -1:
                    print(('Ejemplo: ', sample))
                    print('Clasificación: P2')
        #también tenemos una funcion de apoyo par calcular el signo de un dato.
        def sign(self,u):
            return 1 if u >=0 else -1

#cargamos los datosde ejemplo y las salidas. Se trata de los datos que la neurona aprenderá y el conocimiento que utilizará para clasificar datos desconocidos.

samples = [[1,4],[5,7],[1,3],[6,9],[1,2],[2,1],[8,4],[9,4],[6,8]]
exit = [-1,1,-1,1,-1,-1,1,1,1]

#finalmente usaremos la clase perceptron, creando instancia network y llamamos a l método trainning. El programa solicita por teclado los datos nuevos al usuario para que la neurona clasifique.

network = Perceptron(sample=samples, exit=exit, learn_rate=0.01, epoch_number=1000, bias = -1)
network.training()
while True:
    sample=[]
    for i in range(2):
        sample.insert(i,float(input('Valor:')))
        network.sort(sample)










#IMPLEMENTACION DE DEEP LEARNING

#En esta implementacion nuestro objetivo es predecir la rotación de clientes para un determinado banco, y de esta forma saber que clientes tienen mayor probabilidad de abandonar este servicio bancario.
#El conjunto de datos es relativamente pequeño y contiene 10000 filas con 14 columnas.
#el archivo usado es 09zChurn_Modelling.csv
#utilizamos la distribución anaconda y frames como Theano, TensorFlow y Keras. Keras está construido sobre Tensor FLow y Theano, que funcionan como backends.

#comenzamos instalando esas librerias y cargando datos:
#Artificial Neural Network
#Instalar Theano
#   pip install --upgrade theano
#Instalar TensorFlow
#   pip install --upgrade tensorflow
#INstalar Keras
#   pip install --upgrade keras
# importar las librerias

#importar librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar bbdd
dataset = pd.read_csv('/Users/JAP/Documents/REPOSITORIOS/alwayslearning/learningMachineLearning/09zChurn_Modelling.csv')

#creamos arrays con las caracteristicas (valores) incluidas en el conjunto de datos y la variable objetivo, que es la columna 14, etiquetada como 'Exited'.
X = dataset.iloc[:,3:13].values
Y = dataset.iloc[:,13].values

#para hacer más real el análisis lo simplificamos cofdificando las variables de texto. Estamos utilizando la función ScikitLearn 'LabelEncoder' para codificar automáticamente las diferentes etiquetas en las columnas con valores entre 0 y n_classes-1.

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X_1 = LabelEncoder()
X[:,1] = labelencoder_X_1.fit_transform(X[:,1])
labelencoder_X_2 = LabelEncoder()
X[:,2] = labelencoder_X_2.fit_transform(X[:,2])

#el resultado es la misma bbdd pero con datos codificados en lugar de nombres/textos (Francia=0, Alemania=1 y España=2; masculino =0 y femenino=1)

#Ahora etiquetamos los datos codificados. Usamos la misma biblioteca ScikitLearn y otra función llamada OneHotEncoder para simplemente pasar el número de columna creando una variable ficticia.

onehotencoder = OneHotEncoder(categorical_features = [1])
#en el codigo del curso pone: onehotencoder = OneHotEncoder(categorical_features = [1]) pero categorical_features fue elimanado de OneHotEncoder asi que hay que cambiar el codigo

X = onehotencoder.fit_transform(X).toarray()
X=X[:,1:]
X

#Ahora, las primeras 2 columnas representan el país y la cuarta columna representa el género.
#Siempre dividimos nuestros datos en parte de entrenamiento y pruebas. Utilizaremos la función train-test-split de ScikitLearn para dividir nuestros datos en conjunto de entrenamiento y con junto de prueba. Mantenemos el ratio train_test_split a la proporción 80/20.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size = 0.2)

#algunas variables tienen valores en miles, mietras que otras tienen valores en decenas o unidades. Escalamos los datos par sean más representativos.
#Ajustamos y transformamos los datos de entrenamiento usando la función StandardScaler. Estandarizamos nuetra escla para que se utilice el mismo método ajustado para transformar / escalar datos de prueba.

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Los datos ahora se escalan correctamente. Finalmente, ya tenemos listo el preprocesamiento de los datos. Ahora, comenzaremos con nuestro modelo.
#Importamos los módulos necesarios aquí. Necesitamos el módulo secuencial para inicializar la red neuronal y el módulo dense para agregar las capas ocultas.
#importar Keras y sus paquetes

import Keras
from keras.models import Sequential
from keras.layers import Dense

#el nombre del modelo será 'Classifier' ya que nuestro objetivo es clasificar la rotación de clientes. Luego usamos el módulo secuencial para la inicialización.
#inicializar la red neuronal
classifier = Sequential()
#Agregamos las capas ocultas una por una usando la función dense. EN el siguiente código, veremos muchos argumentos.
#nuestro primer parámetro es output_dim. Es la cantidad de nodos que agregamos a esta capa. init es la inicializacion del gradiente estocástico descendiente.
#en una red neuronal asignamos pesos a cada nodo. En la inicialización, los pesos deben estar cerca de cero y los inicializamos aleatoriamente usando la función uniform. El parámetro input_dim es necesario solo para la primera capa, ya que el modelo no conoce el número de nuestras variables de entrada. Aquí el numero total de variables de entrada es 11. En la segunda capa, el modelo conoce automáticamente el número de variables de entrada de la primera capa oculta. Las siguientes líneas de código agregarán la capa de entrada y la primera capa oculta.

classifier.add(Dense(units=6, kernel_initializer = 'uniform', activation = 'relu' , input_dim = 11))

#agregamos la segunda capa oculta

classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))

#agregamos la capa de salida
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

#ahora vamos a compilar nuestra red. Hasta ahora hemos agregado varias capas a nuestro clasificador. Ahora los compilaremos utilizando el método de compile. Los argumentos agregados en el control de compilación final completan la red neuronal, por lo que debemos ser cuidadosos en este paso.
#a continuación se incluye una breve explicación de los argumentos.
#el primer argumento es Optimizer. Este es un algoritmo utilizado para encontrar el conjunto óptimo de pesos. Este algoritmo se llama Descenso de gradiente estocástico (SGD). Aquí estamos usando uno entre varios tipos, llamado 'Adam optimizer'. El SGD depende de la pérdida, por lo que nuestro segundo parámetro es la pérdida.
#si nuestra variable dependiente es binaria, usamos la función de pérdida logarítmica llamada 'binary_crossentropy', y si nuestra variable dependiente tiene más de dos categorías en la salida, entonces usamos 'categorical_crossentropy'. Queremos mejorar el rendimiento de nuestra red neuronal en función de la precisión, por lo que agregamos métricas como precisión.

#compilar red neuronal.

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#se deben ejecutar varios códigos en este paso.

#ajuste de la red neuronal al conjunto de entrenamiento. Ahora entrenamos nuestro modleo en los datos de entrenamiento. Usamos el método fit para adaptarse a nuestro modelo. También optimizamos los pesos para mejorar la eficiencia del modelo. Para esto, tenemos que acutalizar los pesos. El tamaño del lote (Batch Size) es el número de observaciones después de las cuales actualizamos los pesos. La época (epoch) es el número total de iteraciones. Los valores de tamaño de lote y época se eligen por el método de prueba y error.

classifier.fit(X_train, y_train, batch_siza = 10, epochs =50)

#ya estamos en condiciones de hacer predicciones y evaluar el modelo

#predecir los resultados del test set

y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

#el resultado de la prediccion le dará la probabilidad de que el cliente abandone la empresa. Convertiremos esa probabilidad en binario 0 y 1.
#vamos a predecir sobre una observación
# Geography:Spain
# Credit scaore: 500
# gender: female
# age: 40
# tenure: 3
# balance: 50000
# number of products: 2
# has credit card: yes
#is active member: yes
# todos estos valores se dcodifican, según vimos antes:

new_prediction = classifier.predict(sc.transform(np.array([[0.0,0,500,1,40,3,50000,2,1,1,40000]])))
new_prediction = (new_prediction > 0.5)

#en el último paso evaluamos el rendimiento de nuestro modelo. Ya tenemos resultados originales y, por lo tanto, construir una matriz de confusión para verificar la precisión de nuestro modelo.
#construimos la matriz de confusión

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

#despues de un tiempo de ejecucion obtenemos el resultado
#a partir de la matriz de confusión, la precisión de nuestro modelo se puede calcular como:

# Accuracy = 1531 + 151 / 2000 = 0.841

#logramos una precision del 84,1% lo que es un buen resultado
#podemos ver el resultado de la prediccion con

print(new_prediction)

#el resultado es que el cliente no nos abandona











# ALGORITMO DE PROPAGACIÓN DIRECTA

#En el algoritmo de propagación directa, cada punto de datos es un cliente. La primera entrada es cuantas cuentas tienen, y la segunda entrada es cuantos hijos tienen. El modelo predecirá cuantas transacciones realizará el usuario en el próximo año.
# los datos de entrada se cargan previamente como datos de entrada y los pesos están en un diccionario llamado weights. El array de pesos para el primer nodo en la capa oculta está en pesos ['node_0'], y para el segundo nodo en la capa oculta está en pesos ['node_1'] respectivamente.
#los pesos que se alimentan al nodo de salida están disponibles en weights
#una función de activación es una función que funciona en cada nodo. Transforma la entrada del nodo en alguna salida.
#la función de activación lineal recitificada (llamada ReLU) se usa ampliamente en redes de muy alto rendimiento. Esta función toma un solo número como entrada, devuelve 0 si la entrada es negativa y la entrada como salida si la entrada es positiva.
#aqui algunos ejemplos: relu (4)=4; relu(-2)=0
#completamos la definición de relu() con:
#    usamos la función max() para calcular el valor de la salida de relu()
#    aplicamos la función relu() a node_0_input para calcular node_0_output
#    aplicamos la funcion relu() a node_1_input para calcular node_1_output

#veamos el código:

import numpy as np
input_data = np.array([-1,2])
weights = {'node_0': np.array([3,3]), 'node_1': np.array([1,5]), 'output': np.array([2,-1]) }
node_0_input = (input_data*weights['node_0']).sum()
node_0_output = np.tanh(node_0_input)
node_1_input = (input_data*weights['node_1']).sum()
node_1_output = np.tanh(node_1_input)
hidden_layer_output=np.array(node_0_output, node_1_output)
output = (hidden_layer_output * weights['output']).sum()
print(output)
def relu(input):
    #definir relu fucion de actiacion
    #calcular la salida de la funcion relu: output
    output = max(input,0)
    #remtomar el valor recien calculado
    return(output)
    #calcular valor de node 0: node_0_output
    node_0_input = (input_data*weights['node_0']).sum()
    node_0_output = relu(node_0_input)
    #calcular valor de node 1: node_1_output
    node_1_input = (input_data*weights['node_1']).sum()
    node_1_output = relu(node_1_input)
    #guardar valores en el array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_output, node_1_output])
    #calcular la salida del modelo (sin aplicar relu)
    model_output = (hidden_layer_outputs * weights['output']).sum()
    print(model_output)#mostrar salida del modelo.
#a continuación vamos a desarrollar una función llamada predic_with_network().
#esta función generará predicciones para múltiples observaciones de datos tomadas de la red anterior tomada como input_data. Se están utilizando los pesos dados en la red anterior. La definición de la función relu() también se está utilizando.
#definamos una función llamada predic_with_network() que acepta dos argumentos - input_data_row y weights- y devuelve una prediccion de la red como salida.
#calculamos los valores de entrada y salida para cada nodo, almacenándolos como: node_0_input, node_0_output, node_1_input y node_1_output.
#para calcular el valor de entrada de un nodo, multiplicamos las matrices relevantes y calculamos su suma.
#para calcular el valor de salida de un nodo, aplicamos la función relu() al valor de entrada del nodo. Usamos un 'bucle for' para iterar sobre input_data.
#tambien usamos nuestro predict_with_network() para generar predicciones para cada fila de input_data-input_row. Finalmente, agregamos cada prediccion a los resultados.
#definir predict_with_network()
def predict_with_network(input_data_row, weights):
    #calcular valor node 0
    node_0_input = (input_data_row * weights['node_0']).sum()
    node_0_output = relu(node_0_input)
    #calcular valor node 1
    node_1_input = (input_data_row * weights['node_1']).sum()
    node_1_output = relu(node_1_input)
    #guardar los valores de node en un array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_output, node_1_output])
    #calcular la salida del modelo
    input_to_final_layer = (hidden_layer_outputs*weights['output']).sum()
    model_output = relu(input_to_final_layer)
    #retomar salida del modelo
    return(model_output)
#crear una lista vacia par almacenar los resultados de la prediccion
results=[]
for input_data_row in input_data:
    #agregar prediccion a los resultados
    results.append(predict_with_network(input_data_row, weights))
    print(results)

#usamos la funcion relu donde relu(26)=26 y relu(-13)=0 y asi sucesivamente




#REDES NEURONALES PROFUNDAS MULTICAPA
#vamos a desarrollar un código para hacer propagación hacia adelante para una red neuronal con dos capas ocultas. Cada capa oculta tiene dos nodos. Los datos de entrada se han pregargado como input_data. Los nodos en la primera capa oculta se denominan node_0_0 y node_0_1.
#sus pesos están precargados como weights['node_0_0'] y weights['node_0_1'] respectivamente.
#los nodos en la segunda capa oculta se llaman nodo_1_0 y node_1_1. Sus pesos están precargados como weights['node_1_0'] y weights['node_1_1'] respectivamente.
#luego creamos un modelo de salida de los nodos ocultos usando pesos precargados como weights['output'].
#calculamos node_0_0_input usando sus pesos weights['node_0_0'] y los input_data datos. Luego aplicamos la función relu() para obtener node_0_0_output.
#hacemos los mismo que antes para node_0_1_input para obtener node_0_1_output
#calculamos node_1_0_input usando sus pesos weights ['node_1_0'] y las salidas de la primera capa oculta: hidden_0_outputs. Luego aplicamos la función relu() para obtener node_1_0_output.
#hacemos los mismo que antes para node_1_1_input para obtener node_1_1_output
#calculamos model_output usando pesos ['output'] y los resultados de la segunda capa oculta array hidden_1_outputs. No aplicamos la función relu() a esta salida.

import numpy as np
input_data = np.array([3,5])
weights={
    'node_0_0': np.array([2,4]),
    'node_0_1': np.array([4,-5]),
    'node_1_0': np.array([-1,1]),
    'node_1_1': np.array([2,2]),
    'output': np.array([2,7]),
}

def predict_with_network(input_data):
    #calcular node 0 en la primera capa oculta
    node_0_0_input = (input_data*weights['node_0_0']).sum()
    node_0_0_output = relu(node_0_0_input)
    #calcular node 1 en la primera capa oculta
    node_0_1_input = (input_data*weights['node_0_1']).sum()
    node_0_1_output =relu(node_0_1_input)
    #guardar los valores del node values en el array: hidden_0_ouputs
    hidden_0_outputs = np.array([node_0_0_output, node_0_1_output])
    #calcular node 0 en la segunda capa oculta
    node_1_0_input = (hidden_0_outputs*weights['node_1_0']).sum()
    node_1_0_output = relu(node_1_0_input)
    #calcular node 1 en la segunda capa oculta
    node_1_1_input = (hidden_0_outputs*weights['node_1_1']).sum()
    node_1_1_output = relu(node_1_1_input)
    #guardar los valores de node en el array: hidden_1_ouputs
    hidden_1_outputs = np.array([node_1_0_output, node_1_1_output])
    #calcular salida del modelo: model_output
    model_output = (hidden_1_outputs*weights['output']).sum()
    #return la salida del modelo
    return(model_output)
output = predict_with_network(input_data)
print(output)

#la salida es 364


#EJEMPLO DE LA MASTERCLASS

#masterclass 6 (el tutor dio la clase con GOOGLE COLAB)
#REDES NEURONALES
import tensorflow as tf
import numpy as np
celsius=np.array([-40,-10,0,8,15,22,34], dtype=float)
fahrenheit = np.array([-40, 14,32,46,58,71,100], dtype=float)
capa = tf.keras.layers.Dense(units=1, imput_shape=[1])
#units son las neuronas de las capas
#input_shape = las neuronas de salida
modelo = tf.keras.Sequential([capa])
#creamos un modelo secuencial porque nuestro ejemplo es sencillo
#compilamos
optimizer = tf.keras.optimizers.Adam(0,1),loss='mean_squared_error')
#usamos un compilador como ADAM: la idea es que vaya mejorando y no desaprendiendo. Tasa de Aprendizaje=0.1, con valores mayores es posible que se pase, es mejor ir poco a poco

#'mean_squared_error' es una función de perdida y significa poca cantidad de errores grandes es peor que mas cantidad de errores pequeños.
#vamos a entrenarlo
print('comenzando entrenamiento...')
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
#epochs=vueltas de entrenamiento
print('Modelo entrenado')
#vamos a ver un gráfico para ver como ha ido aprendiendo la red con el numero de vueltas que se ha dado a los datos (epochs)
import matplotlib.pyplot as plt
plt.xlabel('Num. vueltas')
plt.ylabel('Magnitud de pérdida')
plt.plot(historial.history('loss'))
#hagamos una prediccion
print('hagamos una prediccion')
resultado=modelo.predict([37.0])
print('El resultado es '+str(resultado)+'fahrenheit')
#vamos a ver que peso y sesgos ha reconocido
print('variables internas del modelo')
print(capa.get_weights())
#el resultado es muy cercano a la realidad que es peso=1.8 y sesgo=32 (ver formula de c a F)

#ahora haremos lo mismo con 2 capas y 3 neuronas
oculta1 =tf.keras.layers.Dense(units=3, imput_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3 )
salida = tf.keras.layers.Dense(units=1)
modelo=tf.keras.Sequential([oculta1, oculta2,salida])
#el resto de codigo es igual
optimizer = tf.keras.optimizers.Adam((0,1),loss='mean_squared_error')
#usamos un compilador como ADAM: la idea es que vaya mejorando y no desaprendiendo. Tasa de Aprendizaje=0.1, con valores mayores es posible que se pase, es mejor ir poco a poco

#'mean_squared_error' es una función de perdida y significa poca cantidad de errores grandes es peor que mas cantidad de errores pequeños.
#vamos a entrenarlo
print('comenzando entrenamiento...')
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
#epochs=vueltas de entrenamiento
print('Modelo entrenado')
#vamos a ver un gráfico para ver como ha ido aprendiendo la red con el numero de vueltas que se ha dado a los datos (epochs)
import matplotlib.pyplot as plt
plt.xlabel('Num. vueltas')
plt.ylabel('Magnitud de pérdida')
plt.plot(historial.history('loss'))
#hagamos una prediccion
print('hagamos una prediccion')
resultado=modelo.predict([37.0])
print('El resultado es '+str(resultado)+'fahrenheit')

#reconocer ropa fashion_mnist zalando