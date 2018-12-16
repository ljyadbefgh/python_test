#自定义的函数，用于供其他类调用

#定义一个函数，获取偶数个数
def count(data):
    d=0
    for i in data:
        if i%2==0:
            d=d+1
    return d
