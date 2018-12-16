#pandas
'''
loc是指location的意思，iloc中的i是指integer
.iloc：根据标签的所在位置，从0开始计数，选取列
loc：根据DataFrame的具体标签选取列
ix：标签与位置混合索引
'''

import pandas as pd
import numpy as np

#读取表格文件并按表格方式显示
str=pd.read_csv("g:/python/iris.csv")
print(str)
#print(str.head()) # 显示前5行
#print(str.loc[0]) # 按名称索引
#print(str.loc[1,"Sepal.Length"])#获取第二行，Sepal.Length列的单元格数据
#print(str.iloc[3,2]) # 按位置索引，第四行（注意不包括标题行），第三列
#print(str.loc[str["Species"] == "virginica"]) # 按TRUE False 索引,显示Species列为virginica的行
print(str.loc[(str["Species"] == "virginica")&(str["Sepal.Width"]>2)]) # 按TRUE False 索引,显示Species列为virginica并且Sepal.Width>2的行
#print(str.loc[str["Sepal.Width"] > 4] )# 按TRUE False 索引,Sepal.Width列的值>4的行

#分类，聚合
#print(str.groupby("Species").apply(np.mean)) #对Species中的值分组，然后分别计算各组的平均值


