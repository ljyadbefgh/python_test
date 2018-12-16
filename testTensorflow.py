#成功解决本电脑出现的：Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX AVX2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#成功解决本电脑出现的：Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX AVX2
#测试tensorflow是否安装好
import tensorflow as tf
a = tf.constant('hello world!')
sess = tf.Session()
print(sess.run(a))
sess.close()