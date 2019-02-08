import tensorflow as tf

x = tf.placeholder(shape=[], dtype=tf.float32)
y = x + 2

with tf.Session() as sess:
    print(sess.run([x, y], feed_dict={x: 2}))

