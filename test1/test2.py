#对序列[1,2,6,0.3,2,0.5,-1,2.4]按从小到大顺序进行排列。
list = [1,2,6,0.3,2,0.5,-1,2.4]
for i in range(len(list)-1):
    for j in range(len(list)-i-1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]#a,b = b,a,python特有的两个值交换方法，也可以用类似C，java的方法做
print(list)