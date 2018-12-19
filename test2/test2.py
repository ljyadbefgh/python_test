'''
essage80.csv是短信列表（没有列名）
stoplist.txt里面的词是要过滤掉的
'''

import pandas as pd
import jieba

#读取表格中的数据——短信
data = pd.read_csv("message80.csv",header=None) #因为文件没有列名，所以用header=None表示不获取列名称，即数据从第一行起获取
data.columns = ['id','label','message'] # 设置修改列名称
#data.head(3)显示前面3行
#print(data.head(3))

# 将短信分类分别列出
data1 = data.loc[data['label'] == 0] # 正常短信行数据
data2 = data.loc[data['label'] == 1] # 垃圾短信行数据
#将数据抽样，如果系统性能不行可以将数量降低
data1 = data1.iloc[:1000] # 前1000条
data2 = data2.iloc[:1000]
#将上述两种分类抽样出的短信拼接到一起
data = data1.append(data2) #append拼接
#对短信内容进行分词
data['message'] = data['message'].apply(jieba.cut).apply(list) # 分词

#load_useerdict导入用户词典，通过外部文件
jieba.load_userdict("newdic1.txt")


#将保存了要过滤的词的文本导入
'''
sep默认是由tab分割的数据,如果是其他可以另改；
engine='python'      默认是c引擎解析,如果使用python引擎,可以解析更丰富的内容;

'''
stop_word = pd.read_table("stoplist.txt",sep="aaaa",encoding='utf-8',engine='python')
stop_word = stop_word.iloc[:,0].tolist() # 去掉分隔符，然后转换为list
# 停用词过滤，将敏感词汇都直接从所有短信中去掉
data["message"] = data['message'].apply(lambda x:[i for i in x if i not in stop_word])#?????
print(data)

'''
词云图是文本结果展示的有利工具，通过词云图的展示可以对短信文本数据分词后的高频词予以视觉上的 强调突出效果，
 从而达到过滤绝大部分的低频词汇文本信息的效果，使得阅读者一眼就可获取到该新闻的 主旨信息
'''
list1 = []#定义一个集合，
for i in range(data.shape[0]):
    list1.extend(data.iloc[i, 2])
data_wordfre = pd.Series(list1).value_counts()
type(data_wordfre)
# 删除无实际意义的词
data_wordfre = data_wordfre.loc[~data_wordfre.index.str.contains("x| ")]
data_wordfre.head()
# 词云图
from scipy.misc import imread
from wordcloud import WordCloud
import matplotlib.pyplot as plt
back_pic = imread("sucai/aixin.jpg")
wc = WordCloud(font_path='C:/Windows/Fonts/simkai.TTF',  # 设置字体
               background_color="white",  # 背景颜色
               max_words=2000,  # 词云显示的最大词数
               mask=back_pic,  # 设置背景图片
               max_font_size=200,  # 字体最大值
               random_state=42,
               )
nor_wordcloud = wc.fit_words(data_wordfre)
plt.figure(figsize=(10,6))
plt.imshow(nor_wordcloud)
plt.axis("off")
#展示图片
#plt.show()
# 保存图片到指定路径
wc.to_file("G:/python/result.jpg")






data['message'] = data['message'].apply(lambda x:' '.join(x)) # 把列表转成字符串
# 划分训练集测试集
from sklearn.model_selection import train_test_split
train_data,test_data,train_label,test_label = train_test_split(
    data['message'],data['label'],test_size=0.2)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
train_cv = cv.fit_transform(train_data)
train_cv = train_cv.toarray()
train_cv.shape
# 贝叶斯算法
from sklearn.naive_bayes import MultinomialNB
model_nb = MultinomialNB()
model_nb.fit(train_cv,train_label)
# 预测值
pre = model_nb.predict(train_cv) # 对训练样本预测
# 正确率
print(sum(pre == train_label) / len(train_label))







