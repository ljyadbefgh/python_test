'''
练习1:求y=sin(x)从0到2*pi，与x轴围成的面积
1. 将各小矩形的高度存放至一列表中 2. 将各高度乘以宽度，得各矩形面积 3. 求和
'''
import math;
n=100
width=math.pi*2/n#math.pi为3.1415……
x=[i*width for i in range(n)] #x轴坐标
y=[math.sin(i) for i in x]#y轴坐标
result=sum([width*abs(i) for i in y])
print(result)