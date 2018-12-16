'''
熟悉python代码，入门第一个，主要是看懂
代码意思：将helloworldn内容写入已经存在的txt文件中
'''
str="hello world"
file=open("g:/python/hello.txt","w")
file.write(str)
file.close()