import tensorflow as tf

new_g = tf.Graph()
with new_g.as_default():
    a_g = tf.constant(10)
    b_g = tf.constant(10)
    c_g = tf.add(a_g, b_g)

print(a_g.graph)

with tf.Session() as sess:
    sum_t = sess.run(c_g)
    print(sum_t)
