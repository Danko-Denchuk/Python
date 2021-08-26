import tensorflow as tf
import numpy as np
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

celsius = np.array([-40,-10,0,8,15,22,38], dtype=float)
farenheit = np.array([-40,14,32,46,59,72,100], dtype=float)

# capa=tf.keras.layers.Dense(units=1, input_shape=[1])
# modelo=tf.keras.Sequential([capa])

oculta1= tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2= tf.keras.layers.Dense(units=3)
salida=tf.keras.layers.Dense(units=1)
modelo=tf.keras.Sequential([oculta1,oculta2,salida])

modelo.compile(
    tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Starting training")
historial=modelo.fit(celsius, farenheit, epochs=1000, verbose=False)
print("Training finished")

import matplotlib.pyplot as plt
plt.xlabel("Epoch")
plt.ylabel("Loss magnitude")
plt.plot(historial.history["loss"])
plt.savefig("historial.png")

print("Let us make a prediction")
resultado=modelo.predict([100.0])
print("The result is" + str(resultado) + "farenheit")

print("Internal variables of the model")
print(oculta1.get_weights())
print(oculta2.get_weights())
print(salida.get_weights())
