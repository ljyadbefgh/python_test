#垃圾短信分类案例1:对一个短信进行分词

import jieba

str1="带给我们大常州一场壮观的视觉盛宴"
#对上面的短信内容进行分词
#jieba.cut()：第一个参数为需要分词的字符串，第二个cut_all控制是否为全模式。
#list() 方法用于将元组转换为列表。
list1=list(jieba.cut(str1))
print(list1)
'''从上述的分词结果
['带给', '我们', '大', '常州', '一场', '壮观', '的', '视觉', '盛宴']
可以看出，大常州 这个地名无法正确分词
下面为词库添加这个词语即可正确分词
'''
#jieba.add_word("大常州")
list2=list(jieba.cut(str1))
print(list2)
'''
一个一个添加太麻烦，可以将自己的词典用文件放进来，将外部词典导入
'''
#load_useerdict导入用户词典，通过外部文件
jieba.load_userdict("newdic1.txt")
list3=list(jieba.cut(str1))
print(list3)
