import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#importando datos
temperatura_df = pd.read_csv('temperaturas.csv')


#Visualizar datos
sns.scatterplot(temperatura_df['Celsius'], temperatura_df['Farenheit'])

#Entrenamiento de IA
X_train = temperatura_df['Celsius']
Y_train = temperatura_df['Farenheit']

#Creacion del modelo de una sola neurona
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

#model.summary()

#Modelo de compilacion teniendo en cuenta la perdida del error medio cuadrado
model.compile(optimizer=tf.keras.optimizers.Adam(1), loss='mean_squared_error')

#Entrenamiento del modelo IA
epochs_hist = model.fit(X_train, Y_train, epochs=100)

#Evaluacion del Modelo
epochs_hist.history.keys()

#Grafico
plt.plot(epochs_hist.history['loss'])
plt.title('Progreso de perdida durante el entrenamiento')
plt.xlabel('epochs')
plt.ylabel('Training loss')
plt.legend('Training loss')

model.get_weights()

#Predicciones
Temp_c = 0
Temp_f = model.predict([Temp_c])
print(Temp_f)






















