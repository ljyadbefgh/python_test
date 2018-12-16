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
