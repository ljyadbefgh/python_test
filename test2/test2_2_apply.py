#apply函数的练习
'''
apply(func [, args [, kwargs ]]) 函数用于当函数参数已经存在于一个元组或字典中时，间接地调用函数。
args是一个包含将要提供给函数的按位置传递的参数的元组。如果省略了args，任 何参数都不会被传递，
kwargs是一个包含关键字参数的字典。
apply()的返回值就是func()的返回值，apply()的元素参数是有序的，元素的顺序必须和func()形式参数的顺序一致

'''

'''
练习1：
1.以下lambda等同于以下函数
def func(x):
    return(x+1)
'''
def say():
    print("hello world")
apply(*say)

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
