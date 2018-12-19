'''任务二：SoftMax函数Mnist手写数字识别

'''

import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True) # 独热编码

x_data = tf.placeholder(tf.float32, [None, 784])  # 占位符，用来接收样本自变量
y_data = tf.placeholder(tf.float32, [None, 10])   # 占位符，用来接收样本目标变量
w = tf.Variable(tf.zeros([784, 10]))  # 网络权值
bias = tf.Variable(tf.zeros([10]))    # 网络阈值

y = tf.nn.softmax(tf.matmul(x_data, w) + bias)       # 模型输出
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_data*tf.log(y), axis=1))  # 交叉熵
optimizer = tf.train.GradientDescentOptimizer(0.03)  # 梯度下降法优化器
train = optimizer.minimize(cross_entropy)            # 训练节点

init = tf.global_variables_initializer()   # 定义变量初始化
sess = tf.Session()     # 启动会话
sess.run(init)          # 执行变量初始化操作
for i in range(1001):   # 开始训练
    x_s, y_s = mnist.train.next_batch(100)         # 随机取100个样本
    if i%100==0:
        pre = sess.run(y, feed_dict={x_data:x_s})  # 将训练样本的自变量放入网络产生输出
        acc_tr = sum(np.argmax(y_s, axis=1) == np.argmax(pre, axis=1)) / len(y_s)
        print(i,'次训练的精度：',acc_tr)
    sess.run(train, feed_dict={x_data:x_s, y_data:y_s})      # 模型训练

pre_te = sess.run(y, feed_dict={x_data: mnist.test.images})  # 将测试样本的自变量放入网络产生输出
acc_te = sum(np.argmax(mnist.test.labels, axis=1) == np.argmax(pre_te, axis=1))/len(pre_te)
print('测试精度：',acc_te)
sess.close()
