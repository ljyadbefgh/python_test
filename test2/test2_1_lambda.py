'''lambda函数的练习
lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
lambda所表示的匿名函数的内容应该是很简单的，如果复杂的话，干脆就重新定义一个函数了，使用lambda就有点过于执拗了。
lambda就是用来定义一个匿名函数的，如果还要给他绑定一个名字的话，就会显得有点画蛇添足，通常是直接使用lambda函数。
如下所示：
add = lambda x, y : x+y
add(1,2)  # 结果为3
'''

'''
练习1：
1.以下lambda等同于以下函数
def func(x):
    return(x+1)
'''
func1=lambda x:x+1
print(func1(1))

'''
2.配合其他函数使用
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
说明：关于filter()方法, python3和python2有一点不同。Python2.x 中返回的是过滤后的列表, 而 Python3 中返回到是一个 filter 类。

题目：将列表中的所有奇数显示出
以下代码等价于下面的代码

#定义一个函数，当是奇数时返回true，否则返回false
def count(x):
    return x % 2 == 1
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(list(filter(count,foo)))
'''
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(list(filter(lambda x:x%2==1,foo)))





# list=[1,2,3,4,5]
# func2=lambda list:[i for i in list]
# print(func2)