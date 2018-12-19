import tensorflow as tf
#让数组内的元素相加
#TensorFlow程序的两个阶段
#========1.  定义计算（在计算图中） =====
a=tf.constant([1,2])#constant定义tf常量，后面不能改变，tf必须这样定义
b=tf.constant([3,4])
res=a+b#定义计算方法
print(res)#打印出Tensor("add:0", shape=(2,), dtype=int32)

#2.  执行计算（在会话中）
sess=tf.Session()#启动会话
res1=sess.run(res)#执行计算，并将结果返回
print(res1)