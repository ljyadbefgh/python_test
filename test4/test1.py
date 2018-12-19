import tensorflow as tf
import cv2
import numpy as np
'''
此脚本主要展示卷积神经网络（CNN）的两个核心过程：卷积和池化
'''
img = cv2.imread('0_2.png')   # 读入图片
img = cv2.resize(img, (28, 28))[:,:,0:1]/255
img = np.float32(img.reshape([1, 28, 28, 1]))  # 维度转化

w = tf.Variable(tf.random_normal([3,3,1,32], stddev=0.01))  # 卷积核（filter）
conv = tf.nn.conv2d(img, w, strides=[1,1,1,1], padding='SAME') # 卷积
pool = tf.nn.max_pool(conv, strides=[1,2,2,1], ksize=[1,2,2,1], padding='SAME')  # 池化

sess = tf.Session()
sess.run(tf.global_variables_initializer())
conv1 = sess.run(conv)
pool1 = sess.run(pool)
sess.close()
cv2.imwrite('conv1.jpg', conv1[0,:,:,15]*10000)   # 将卷积结果的第15通道画出来
cv2.imwrite('pool1.jpg', pool1[0,:,:,15]*10000)   # 将池化结果的第15通道画出来
