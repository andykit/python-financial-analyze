# -*- coding: utf-8 -*-
import pandas as pd
dt=pd.read_excel('data2.xlsx')  #获取数据
#选择满足2014~2017年都存在利润数据上市公司股票代码，即存在4个会计年度
code=dt['Stkcd'].value_counts()
code=list(code[code==4].index)
#将股票基本信息表转化为序列，其中index为股票代码，值为股票名称
info=pd.read_excel('info.xlsx')
S=pd.Series(info.iloc[:,1].values,index=info.iloc[:,0].values)
#预定义4个list，依次存放股票名称、2015、2016、2017年的净利润增长率
list1=[]
list2=[]
list3=[]
list4=[]
for t in range(len(code)):
    d=dt.iloc[dt.iloc[:,0].values==code[t],2].values
    r=(d[1:]-d[0:-1])/d[0:-1]
    if len(r[r>0.4])==3:
        list1.append(S[code[t]])
        list2.append(r[0])
        list3.append(r[1])
        list4.append(r[2])
#将净利润增长率数据定义为字典
D={'2015':list2,'2016':list3,'2017':list4}
#将字典转化为数据框，index为股票名称
D=pd.DataFrame(D,index=list1)


