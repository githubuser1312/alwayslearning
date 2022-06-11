import numpy as np 
import matplotlib.pyplot as plt

#Ejemplo de REGRESION LINEAL SIMPLE: y = b_0 + b_1 * x
def estimate_coef(x,y):
    n = np.size(x) #numero de observaciones
    m_x = np.mean(x) #calcula la media aritmética del vector x
    m_y = np.mean(y) #calcula la media aritmética del vector y
    SS_xy = np.sum(y*x)-n*m_y*m_x #calcula la desviación cruzada
    SS_xx = np.sum(x*x)-n*m_x*m_x #calcula la desviación sobre x
    b_1 = SS_xy / SS_xx #calculo de la inclinacion
    b_0 = m_y - b_1*m_x #cálculo del corte sobre el eje
    return(b_0,b_1)
def plot_regression_line(x,y,b):
    plt.scatter(x,y, color="m", marker="o", s=30) #dibujar los puntos en un scatter (dispersion) plot 
    y_pred = b[0] + b[1] * x #vector de prediccion de respuesta
    plt.plot(x, y_pred, color="g")#dibujar línea de regresion
    plt.xlabel('x') #etiqueta de x
    plt.ylabel('y') #etiqueta de y
    plt.show() #mostrar grafica
def main():
    x = np.array([0,1,2,3,4,5,6,7,8,9])#datos
    y = np.array([1,3,2,5,7,8,8,9,10,12])#observaciones
    b = estimate_coef(x,y) #estimacion de coeficientes
    print("Coeficientes estimados:\nb_0 = {} \nb_1 = {}".format(b[0],b[1]))
    plot_regression_line(x,y,b)
    if __name__ == "__main__":
        main()


main()

#Nota: Ejecutar sólo las lineas de código siguientes marcándolas y en el menu contextual elegir Run selection in interactive window

#Ejemplo de REGRESION LINEAL MULTIPLE:
#Conjunto de datos de precios de viviendas de Boston usando Scikit-learn
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model, metrics

boston = datasets.load_boston(return_X_y=False) #carga del dataset de Boston
X = boston.data #definición de la matriz de características
y = boston.target #definición de la matriz de respuesta

from sklearn.model_selection import train_test_split #separación de X e y en conjuntos de entrenamiento y pruebas

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=1)

reg = linear_model.LinearRegression() #crear objeto de regresion lineal
reg.fit(X_train, y_train) #entrenar el modelo utilizando el conjunto de entrenamiento

print('Coeficientes:',reg.coef_)#coeficientes de regresion
print('Medicion de la varianza: {}'.format(reg.score(X_test,y_test))) #medicion de la varianza: 1 significa prediccion perfecta
plt.style.use('fivethirtyeight') #dibujar error residual , plot style
plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train, color='green', s=10, label = 'Datos entrenamiento') #dibujar errores residuales en datos de entrenamiento
plt.scatter(reg.predict(X_test), reg.predict(X_test)- y_test, color='blue', s =10, label = 'Datos prueba') #dibujar errores residuales en datos de prueba
plt.hlines(y=0, xmin = 0, xmax = 50, linewidth = 2) #dibujar linea para error residual cero
plt.legend(loc = 'upper right')#dibujar leyenda
plt.title("Errores residuales") #dibujar título
plt.show() #mostrar


