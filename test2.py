import tensorflow as tf
import numpy as numpy

키 = 168
신발 = 260

a = tf.Variable(0.1)
b = tf.Variable(0.2)


def lossFunc():
    예측값 = 키 * a + b
    return tf.square(260 - 예측값)

opt = tf.keras.optimizers.Adam(learning_rate=0.1)

for i in range(300):
    opt.minimize(lossFunc, var_list=[a, b])
    print(a.numpy(). b.numpy())


