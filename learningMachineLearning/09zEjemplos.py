# EJEMPLO DE PERCEPTRON

#vamos a desarrollar un algoritmo que clasifique los vlaores en dos categorías: p1 y p2

#lo primero que haremos será crear una clase llamada "Perceptron", para defnir los atributos del Perceptron:
# Datos de entrenamiento
# Salida esperada
# Otras características
import random

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
