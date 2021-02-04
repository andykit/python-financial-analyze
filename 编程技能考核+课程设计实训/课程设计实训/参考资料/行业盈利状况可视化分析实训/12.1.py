# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
font={'family':'SimHei'}#为了便于图中显示中文
matplotlib.rc('font',**font)

data=pd.read_excel('公司净利润数据表.xlsx')
td=pd.read_excel('申万行业分类表.xlsx')
name=td['行业名称'].value_counts()
name=list(name.index)
D=np.zeros((len(name),7))
D1=np.zeros((len(name),6))
for i in range(len(name)):
    s=td.loc[td['行业名称'].values==name[i],'股票代码'].values
    for y in range(2011,2018):
        date=str(y)+'-12-31'
        stk=data.loc[data['Accper'].values==date,'Stkcd'].values
        lr=data.loc[data['Accper'].values==date,'B002000101'].values
        S=pd.Series(lr,index=stk)
        D[i,y-2011]=S[s].sum()

for k in range(len(name)):
    D1[k,:]=(D[k,1:]-D[k,:-1])/D[k,:-1]
D1=pd.DataFrame(D1,index=name)

'''
for i in range(6):
    plt.figure(i)
    q=D1[i].sort_values()[-8:]
    plt.bar([1,2,3,4,5,6,7,8],q.values)
    plt.xticks([1,2,3,4,5,6,7,8],q.index,rotation=40)
'''
plt.figure(1)
plt.figure(figsize=(10,8))
for i in range(6):
    plt.subplot(3,2,i+1)
    plt.title(str(2012+i)+'年净利润增长率前8的行业')
    plt.tight_layout() 
    q=D1[i].sort_values()[-8:]
    plt.bar([1,2,3,4,5,6,7,8],q.values)
    plt.xticks([1,2,3,4,5,6,7,8],q.index,rotation=45)
plt.savefig('1')
    
    
    
    
