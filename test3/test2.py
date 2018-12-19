from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
iris = load_iris()   # 鸢尾花数据
'''
train_test_split函数用于将矩阵随机划分为训练子集和测试子集，并返回划分好的训练集测试集样本和训练集测试集标签。
train_data：被划分的样本特征集
train_target：被划分的样本标签
test_size：如果是浮点数，在0-1之间，表示样本占比；如果是整数的话就是样本的数量
random_state：是随机数的种子,如果是相同的话，取数是一致的
随机数种子：其实就是该组随机数的编号，在需要重复试验的时候，保证得到一组一样的随机数。比如你每次都填1，其他参数一样的情况下你得到的随机数组是一样的。但填0或不填，每次都会不一样。
随机数的产生取决于种子，随机数和种子之间的关系遵从以下两个规则：
种子不同，产生不同的随机数；种子相同，即使实例不同也产生相同的随机数。
'''
data_tr, data_te, target_tr, target_te = \
    train_test_split(iris.data, iris.target, test_size=0.2) # 拆分数据

model = DecisionTreeClassifier(random_state=0)
model.fit(data_tr, target_tr)   # 模型训练
pre = model.predict(data_te)    # 模型预测

acc_te = sum(pre==target_te)/len(pre)  # 测试精度
print(acc_te)
# res = iris.data
# res1 = iris.target
# print(target_te)
# print(sum(pre==iris.target)/150)
# print(iris.target)
