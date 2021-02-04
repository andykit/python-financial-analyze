# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
data=pd.read_excel('国际股票价格指数日交易数据表.xlsx')
code=list(data.iloc[:,0].value_counts().index)
D=dict()
tdate=[]
for c in code:
    dt=data.loc[data['Indexcd'].values==c,['Trddt','Clsidx']].sort_values('Trddt')
    p1=dt['Clsidx'].values[:-1]
    p2=dt['Clsidx'].values[1:]
    z=np.zeros(len(p1))
    z[(p2-p1)/p1>=0.005]=1
    S=pd.Series(z,index=dt['Trddt'].values[1:])
    D.setdefault(c,S)
    if c=='000300':
        tdate.extend(list(dt['Trddt'].values[1:]))
DT=dict()
Tf=[]
for t in tdate:
    tz=True;
    for k in code:
        s=D.get(k)
        s=list(s.index)
        sz=t in s
        tz=tz and sz
    if tz==True:
       Tf.append(t)

DA=dict()
for k in code:
    s=D.get(k)
    DA.setdefault(k,s[Tf].values)
Data=pd.DataFrame(DA,index=Tf)

c=list(Data.columns) 
c0=0.6 #最小置信度
s0=0.1 #最小支持度
list1=[] #预定义定义列表list1，用于存放规则
list2=[] #预定义定义列表list2，用于存放规则的支持度
list3=[] #预定义定义列表list3，用于存放规则的置信度
for k in range(len(c)):
    for q in range(len(c)):
        #对第c[k]个项与第c[q]个项挖掘关联规则
        #规则的前件为c[k]
        #规则的后件为c[q]
        #要求前件和后件不相等
        if c[k]!=c[q]:
           c1=Data[c[k]]
           c2=Data[c[q]]
           I1=c1.values==1
           I2=c2.values==1
           t12=np.zeros((len(c1)))
           t1=np.zeros((len(c1)))
           t12[I1&I2]=1
           t1[I1]=1
           sp=sum(t12)/len(c1) #支持度
           co=sum(t12)/sum(t1) #置信度
           #取置信度大于等于c0的关联规则
           if co>=c0 and sp>=s0:
              list1.append(c[k]+'--'+c[q])
              list2.append(sp)
              list3.append(co)
#定义字典，用于存放关联规则及其置信度、支持度   
R={'rule':list1,'support':list2,'confidence':list3}
#将字典转化为数据框
R=pd.DataFrame(R)
#将结果导出到Excel
R.to_excel('rule1.xlsx')

import apriori as ap
support = 0.08 #最小支持度
confidence = 0.9 #最小置信度
ms = '--' #连接符，
outputfile = 'apriori_rules.xls' #结果文件
ap.find_rule(Data, support, confidence, ms).to_excel(outputfile) #联动


