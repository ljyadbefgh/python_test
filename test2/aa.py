'''
essage80.csv是短信列表（没有列名）
stoplist.txt里面的词是要过滤掉的
'''

import pandas as pd
import jieba
data = pd.read_csv("G:/python/message80.csv",header=None) #因为文件没有列名，所以用header=None表示不获取列名称，即数据从第一行起获取
data.columns = ['id','label','message'] # 设置修改列名称
data.head()
# 将短信分类分别列出
data1 = data.loc[data['label'] == 0] # 正常短信行数据
data2 = data.loc[data['label'] == 1] # 垃圾短信行数据
#将数据抽样
data1 = data1.iloc[:10000] # 前10000条
data2 = data2.iloc[:10000]
#将上述两种分类抽样出的短信拼接到一起
data = data1.append(data2) # 拼接
#对短信内容进行分词
data['message'] = data['message'].apply(jieba.cut).apply(list) # 分词

#load_useerdict导入用户词典，通过外部文件
jieba.load_userdict("G:/python/newdic1.txt")


#将保存了要过滤的词的文本导入
'''
sep默认是由tab分割的数据,如果是其他可以另改；
engine='python'      默认是c引擎解析,如果使用python引擎,可以解析更丰富的内容;

'''
stop_word = pd.read_table("G:/python/stoplist.txt",sep="aaaa",encoding='utf-8',engine='python')
stop_word = stop_word.iloc[:,0].tolist() # 去掉分隔符，然后转换为list
# 停用词过滤，将敏感词汇都直接从所有短信中去掉
'''
lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
lambda所表示的匿名函数的内容应该是很简单的，如果复杂的话，干脆就重新定义一个函数了，使用lambda就有点过于执拗了。
lambda就是用来定义一个匿名函数的，如果还要给他绑定一个名字的话，就会显得有点画蛇添足，通常是直接使用lambda函数。
如下所示：
add = lambda x, y : x+y
add(1,2)  # 结果为3
'''
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
back_pic = imread("G:/python/aixin.jpg")
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
plt.show()