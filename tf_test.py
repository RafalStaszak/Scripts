import tensorflow as tf
import numpy as np


a = tf.Variable(np.eye(100))
b = tf.Variable(np.eye(100))
c = tf.matmul(a, b)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(10000000):
        sess.run(c)