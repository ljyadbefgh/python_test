'''
练习3：小说《Walden》单词词频统计
Walden中文译名《瓦尔登湖》，是美国作家梭罗独居瓦尔登湖畔的记录，描绘了他两年多时间里的所见、所 闻和所思。该书崇尚简朴生活，
热爱大自然的风光，内容丰厚，意义深远，语言生动。请用Python统计小说 Walden中各单词出现的频次，并按频次由高到低排序。

案例更改：统计里面各单词的出现频率，大小写不限
'''
content = 'The night begin to shine, the night begin to shine'
content=content.lower();#都转换为小写
words=content.split()#通过指定分隔符对字符串进行切片，根据空格来分隔单词,
print(words)#输出分隔后的单词


