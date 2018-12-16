'''
2006年，NumPy v1.0
NumPy 是一个运行速度非常快的数学库，主要用于数组计算，包含：

一个强大的N维数组对象 ndarray
广播功能函数
整合 C/C++/Fortran 代码的工具
线性代数、傅里叶变换、随机数生成等功能

ndarrary：NumPy库的心脏
 ndarray：多维数组，具有矢量运算能力，且快速、节省空间
 可对整组数据进行快速运算的标准数学函数、线性代数、随机数生成等功能
 import numpy as np

1.arrange()函数

函数说明：arange([start,] stop[, step,], dtype=None)根据start与stop指定的范围以及step设定的步长，生成一个 ndarray。 d

题目：平面上有100个点，求任意2点间的距离，并将其保存。
'''
import numpy as np

x = np.arange(100) # x轴坐标
print("x轴坐标:",x);
y = np.arange(100,200) # y轴坐标
print("y轴坐标:",y);
dict1 = np.zeros([100,100]) # 全0矩阵，100*100
print(dict1)
for i in range(100):
    for j in range(100):
        dict1[i,j] = ((x[i] - x[j])**2 + (y[i] - y[j])**2)**0.5#求两点间距离的长度公式
print(dict1)

