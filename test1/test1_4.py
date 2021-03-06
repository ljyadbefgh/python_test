'''
for循环和range的使用
range() 函数可创建一个整数列表，一般用在 for 循环中。
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;0,1,2,3,4
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''

for count in range(1,6):
    print(count)
for count in range(0,100,10):
    print(count)
for count in range(6):
    print(count)
array=[count+6 for count in range(0,3)]
print(array)
#将每次循环的值count存入数组array1
array1=[count for count in range(1,10)]
print(array1)
#将每次循环的值count*10，即计算后再存入数组array2
array2=[count*10 for count in range(1,10)]
print(array2)
#将每次循环count>5的值，count*10，即计算后再存入数组array2
array3=[count*10 for count in range(1,10) if count>5]
print(array3)