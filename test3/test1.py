#sklearn API文档地址：https://scikit-learn.org/stable/modules/classes.html
from sklearn.datasets import load_iris
#DecisionTreeClassifier分类器，
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
iris = load_iris()   # 鸢尾花数据

model = DecisionTreeClassifier(random_state=0)
#res=iris.data
#res1=iris.target
#res.shape表示几行几列，输出如(150, 4)，(150,)
#print(res.shape)
#print(res1.shape)
model.fit(iris.data, iris.target)   # 模型训练
#而predict(start,end)里面的参数0表示样本内的第一个数，
# 以此类推。如果想要预测样本外的数，需要将start设置为len(data)+1,即数据长度+1，才表示预测样本外的第一个数字。
pre = model.predict(iris.data)
print(sum(pre==iris.target)/len(iris.data))
