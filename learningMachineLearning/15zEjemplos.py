#IMPLEMENTACION DEL ANÁLISIS DE CESTA

#Los datos específicos del ejemplo provienen del Repositorio de Aprendizaje Automático de la UCI y representan datos transaccionales de un minorista del Reino Unido de 2010-2011. Esto representa principalmente las ventas a mayoristas, por lo que es ligeremanente diferente de los patrones de compra del consumidor, pero sigue siendo un caso de estudio útil.

#El objetivo es utilizar esta biblioteca para analizar un conjunto de datos minoritstas en línea relativamente grande e intentar encontrar combinaciones de compra interesantes.

#El dataset es bastante grande por que puede tardar varios minutos.

#instalamos MLxtend con pip (1 vez y comento la linea)
#pip install mlxtend

#una vez instalado el código siguiente muestra como ponerlo en marcha.

#importamos pandas y MLxtend y leemos los datos:

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

#df = pd.read_excel('http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online Retail.xlsx')

df = pd.read_excel('learningMachineLearning/14zOnline Retail.xlsx')

df.head()

#para ordenar un poco los datos hay que eliminar algunas de las descripciones. También eliminaremos las filas que no tienen número de factura y eliminaremos las transacciones de crédito (aquellas con números de factura que contengan C).

df['Description'] = df['Description'].str.strip()
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
df['InvoiceNo']=df['InvoiceNo'].astype('str')
df=df[~df['InvoiceNo'].str.contains('C')]


#después de la limpieza, necesitamos consolidar los elementos en 1 transacción por fila con cada producto codificado en ONE HOT. E n aras de mantener el conjunto de datos pequeño, sólo trabajaremos con las ventas de Francia. Sin embargo, en el código después se compararán estos resultados con las ventas de Alemania. Sería interesante investigar más comparaciones de paises.


basket = df[df['Country'] == "France"].groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().reset_index().fillna(0).set_index('InvoiceNo')

#hay muchos ceros en los datos, pero también debemos asegurarnos de que los valores positivos se conviertan en 1 y cualquier cosa menos que el 0 se establezca en 0. Este paso completará la codificacion ONE HOT de los datos y eliminará la columna de franqueo - postage (ya que ese cargo no es uno que deseemos explorar):

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
basket_sets.drop('POSTAGE', inplace=True, axis=1)

#ahora que los datos están estructurados correctamente, podemos generar conjuntos de elementos frecuentes que tengan un soporte de al menos el 7% (este numero nos permite obtener suficientes ejemplos útiles):

frequent_itemsets = apriori(basket_sets, min_support=0.07, use_colnames=True)

#el paso final es generar las reglas con su correspondiente apoyo, confianza y lift:

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.head()

#ahora viene la parte de interpretar los datos. Por ejemplo, podemos ver que hay bastantes reglas con un alto valor de elevación, lo que significa que ocurre con más frecuencua de lo que cabría esperar dado el número de combinaciones de transacciones y productos. También podemos ver varios datos donde la confianza es alta también. Esta parte del análisis es donde el conocimiento del dominio será útil.

#podemos filtrar el dataframe usando código pandas estándar. En este caso, buscamos un lift grande (6) y una alta confianza(.8):

rules[(rules['lift'] >= 6) & (rules['confidence'] >= 0.8)]

#al observar las reglas, parece que lo despertadores verdes y rojos se compran juntos con una frecuencia más alta de lo que sugeriría la probabilidad general.

#En este punto, es posible que deseemos ver cuánta oportunidad hay que utilizar la popularidad de un producto para impulsar las ventas de otro. Por ejemplo, podemos ver que vendemos 340 despertadores verdes, pero solo 316 despertadores rojos, así que tal vez podamos impulsar más ventas de relojes despertadores rojos a través de recomendaciones.

basket['ALARM CLOCK BAKELINE GREEN'].sum()
basket['ALARM CLOCK BAKELINE RED'].sum()

#lo que también es interesante es ver como varían las combinaciones según el país de compra. Echemos un vistazo a algunas combinaciones populares en Alemania:

basket2 = (df[df['Country'] == "Germany"].groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack.reset_index().fillna(0)).set_index('InvoiceNo')

basket_sets2 = basket.applymap(encode_units)
basket_sets2.drop('POSTAGE', inplace=True, axis=1)

frequent_itemsets2 = apriori(basket_sets2, min_support=0.05, use_colnames=True)

rules2 = association_rules(frequent_itemsets2, metric="lift", min_threshold=1)

rules2[(rules2['lift'] >= 4) & (rules2['confidence'] >= 0.5)]

#parece que los alemanes prefieren Plasters in Tin Spaceboy y Woodland Animals.

