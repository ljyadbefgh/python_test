'''
练习3：小说《Walden》单词词频统计
Walden中文译名《瓦尔登湖》，是美国作家梭罗独居瓦尔登湖畔的记录，描绘了他两年多时间里的所见、所 闻和所思。该书崇尚简朴生活，
热爱大自然的风光，内容丰厚，意义深远，语言生动。请用Python统计小说 Walden中各单词出现的频次，并按频次由高到低排序。

案例更改：统计里面各单词的出现频率，大小写不限,并按频次由高到低排序
'''
import re
content = 'The night begin to shine, the night begin to shine shine ' \
          'The night begin to shine, the night'
#都转换为小写
content=content.lower()
#将字符串打断成单词
words=content.split(" ")
print(words)
#去掉单词中的标点符号，注意不能直接在文章内容没有切割以前转，否则容易出现重复，例如abc,abc，就变成了abcabc，而不是abc abc两个元素
#re.sub()是正则表达式的函数，实现比普通字符串更强大的替换功能.此处用于将文章中的符号去掉
words=[re.sub("[,'.:;]",'',word) for word in words]
#将重复的words单词去掉
words_index=set(words)
map={word:content.count(word) for word in words}
print(map)#输出分隔后的单词

#对出现频率进行排序


