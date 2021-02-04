####行业联动
import pandas as pd
x=pd.read_excel('交易日历数据表.xlsx')
x=x.iloc[:1741,:]
list1=['2010-01-04']
list2=[]
for t in range(1,len(x)-1):
    p=x.iloc[t-1,[2]][0]
    q=x.iloc[t,[2]][0]
    if q<p:
        list1.append(x.iloc[t,[1]][0])
        list2.append(x.iloc[t-1,[1]][0])
list1=list1[:-1]

codename=pd.read_excel('指数基本信息表.xlsx')
sname=pd.Series(list(codename.iloc[:,1]),index=codename.iloc[:,0])

data=pd.read_excel('指数交易数据表20100104-20170307.xlsx')
code_record=data.iloc[:,0].value_counts()
code=list(code_record[code_record==1741].index)

import numpy as np
D=dict()
for t in range(len(code)):
   dt=data.loc[data['指数代码']==code[t],['交易日期','收盘价']].sort_values('交易日期')
   z=np.zeros((len(list1)))
   for i in range(len(z)):
       a2=dt.loc[dt['交易日期']==list2[i],['收盘价']]['收盘价']
       a1=dt.loc[dt['交易日期']==list1[i],['收盘价']]['收盘价']
       z[i]=a2.values-a1.values
   z[z>0]=1
   z[z<=0]=0
   D.setdefault(sname[code[t]]+'_up',z)
Data=pd.DataFrame(D)

import apriori as ap
support = 0.47 #最小支持度
confidence = 0.9 #最小置信度
ms = '--' #连接符，
outputfile = 'apriori_rules2.xls' #结果文件
ap.find_rule(Data, support, confidence, ms).to_excel(outputfile) 

import OneRule as OR
r=OR.rule(Data,0.2,0.58)

'''
####行业轮动
#获取字段名称（行业名称_up），并转化为列表
c=list(Data.columns) 
list1=[] #预定义定义列表list1，用于存放规则
list2=[] #预定义定义列表list2，用于存放规则的支持度
list3=[] #预定义定义列表list3，用于存放规则的置信度
for k in range(len(c)):
    for q in range(len(c)):
        #对第c[k]个行业与第c[q]个行业计算行业轮动规则
        #规则的前件为c[k]
        #规则的后件为c[q]，计算周期与c[k]需后移一个周期
        c1=Data[c[k]][0:-1]
        c2=Data[c[q]][1:]
        I1=c1.values==1
        I2=c2.values==1
        t12=np.zeros((len(c1)))
        t1=np.zeros((len(c1)))
        t12[I1&I2]=1
        t1[I1]=1
        sp=sum(t12)/len(c1) #支持度
        co=sum(t12)/sum(t1) #置信度
        #取置信度大于0.58的关联规则
        if co>0.58:
           list1.append(c[k]+'--'+c[q])
           list2.append(sp)
           list3.append(co)
           
#定义字典，用于存放关联规则及其置信度、支持度   
R={'rule':list1,'support':list2,'confidence':list3}
#将字典转化为数据框
R=pd.DataFrame(R)
#将结果导出到Excel
R.to_excel('rule2.xlsx')
'''

        
    
    