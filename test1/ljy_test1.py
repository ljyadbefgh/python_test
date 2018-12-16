#为多个变量赋值
name,sex,age="张三","男",20
print(name,sex,age)
#数值计算
a,b=8,5
print(a/b)# 除法，得到一个浮点数
print(a//b)#除法，得到一个整数

#字符串练习：Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
str="HelloWorld"
print(str)# 输出字符串
print(str[0])# 输出字符串第一个位置
print(str[1:4]) #输出从第二个开始到第五个的字符
print(str.count("o")) #统计o出现了几次