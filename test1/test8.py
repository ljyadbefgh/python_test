'''
连接，左连接，右连接
'''
import pandas as pd
import numpy as np
#连接
data1=pd.DataFrame({"key":['k1',"k2",'k3'], "value1":[3,4,5]});
print(data1)
data2=pd.DataFrame({"key":['k1',"k12",'k3','k4'],"value2":[4,5,6,7]})
print(data2)
#左连接
print(data1.merge(data2,how='left',on="key"))
#右连接
print(data1.merge(data2,how='right',on="key"))
#内连接
print(data1.merge(data2,how='inner',on="key"))
#外连接
print(data1.merge(data2,how='outer',on="key"))

