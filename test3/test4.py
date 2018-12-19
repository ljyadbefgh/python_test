'''

# 任务1:拟合三维平面
步骤
1.  
利用 Numpy 生成 100 个样本点
2.  
构造一个线性模型
3.  
最小化方差
4.  
初始化变量
5.  
启动图
6.  
拟合平面 ( 开始训练
'''


import numpy as np
import tensorflow as tf

#1.利用 Numpy 生成 100 个样本点
data=np.load('sucai/line_fit_data.npy')
data=np.float32(data)#转换为32位，不然计算可能出错
x_data=data[:,0:2]#获取所有行，1-2列的数据
y_data=data[:,2:]#获取所有行，3列及以后的数据

#2.构造一个线性模型
#zeros 创建一个m行n列的数组并初始化它们都为0
#tf.Variable()返回一个tf.Variable类的实例。定义tf变量，tf必须这样定义
w=tf.Variable(tf.zeros([2,1]))# 模型的权值（系数）
bias=tf.Variable(tf.zeros([1]))# 模型的偏置项（截距）
#tf.matmul，将矩阵 a 乘以矩阵 b，生成a * b
y=tf.matmul(x_data,w)+bias  # y = a*x1 + b*x2 + c

#3.最小化方差
loss=tf.reduce_mean(tf.square(y_data-y)) # 损失函数
optimizer = tf.train.GradientDescentOptimizer(0.5)  # 梯度下降法优化器（0.5是学习速率）
train = optimizer.minimize(loss)    # 训练的节点

#4.初始化变量
init=tf.global_variables_initializer()#初始化之前的所有变量(w,bias,y)，不然无法运行

#5.启动图
sess=tf.Session()
sess.run(init)  # 执行变量初始化操作

#6.拟合平面 ( 开始训练）
for i in range(100):
    print(i,'次训练的loss：',sess.run(loss))
    sess.run(train)    # 6.  拟合平面(开始训练)
print(sess.run([w,bias]))
sess.close()

