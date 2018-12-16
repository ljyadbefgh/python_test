#列表List的增删改查
students=['张三','李四','小红',"小军"]
#输出第一个元素
print(students[0])
#输出倒数第一个元素
print(students[-1])
#输出第2个和第3个元素），注意，3不包含4位置。类似>=1,<3
print(students[1:3])
#在数组末尾添加一个元素
students.append("小李")
print(students)
#删除数组中的一个元素
del students[1]#删除数组中的第二个元素
print(students)
del students[0:2]#删除数组中的第二个和第四个元素
print(students)
#修改数组中的一个元素
students[1]="老李"
print(students)
'''
range() 函数可创建一个整数列表，一般用在 for 循环中。
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''

for count in range(2,10):
    print(count)
for count in range(0,100,10):
    print(count)
#将每次循环的值count存入数组array1
array1=[count for count in range(1,10)]
print(array1)
##将每次循环的值count*10，即计算后再存入数组array2
array2=[count*10 for count in range(1,10)]
print(array2)