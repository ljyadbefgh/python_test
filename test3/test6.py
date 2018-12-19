import tensorflow as tf
import cv2
import numpy as np
tf.reset_default_graph()

path = 'testimages/'
imgNames = ['0.jpg','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg']

sess = tf.Session()
saver = tf.train.import_meta_graph('temp/train_model.meta')  # 导入计算图
saver.restore(sess, 'temp/train_model')    # 激活计算图（将所有模型参数导进来）
graph = tf.get_default_graph()             # 获取当前计算图
x_data = graph.get_tensor_by_name('input:0')  # 通过名称寻找保存好的tensor作为网络入口
y = graph.get_tensor_by_name('output:0')      # 通过名称寻找保存好的tensor作为网络出口

for i in imgNames:
    img = cv2.imread(path + i)[:, :, 0] / 255    # 读入图片
    img = np.float32(img.reshape([1, 28 * 28]))  # 转成要求的shape
    pre = sess.run(y, feed_dict={x_data:img})    # 调用模型进行预测
    number = np.argmax(pre)                      # 输出的数字
    print('图片',i,'是数字：',number)
sess.close()
