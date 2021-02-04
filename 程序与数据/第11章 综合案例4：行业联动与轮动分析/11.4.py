####行业联动
import pandas as pd
codename=pd.read_excel('指数基本信息表.xlsx')
sname=pd.Series(list(codename.iloc[:,1]),index=codename.iloc[:,0])

data=pd.read_excel('指数交易数据表20100104-20170307.xlsx')
code_record=data.iloc[:,0].value_counts()
code=list(code_record[code_record==1741].index)

import numpy as np
D=dict()
for t in range(len(code)):
   dt=data.loc[data['指数代码']==code[t],['交易日期','收盘价']].sort_values('交易日期')
   dt1=dt.iloc[0:-1,[1]]['收盘价'];
   dt2=dt.iloc[1:,[1]]['收盘价'];
   z21_up=np.zeros(len(dt1))
   z21_up[dt2.values-dt1.values>0]=1
   D.setdefault(sname[code[t]]+'_up',z21_up)

td=pd.read_excel('交易日历数据表.xlsx')
Data=pd.DataFrame(D,index=td['Clddt'].values[1:1741])

import apriori as ap
support = 0.47 #最小支持度
confidence = 0.9 #最小置信度
ms = '--' #连接符，
outputfile = 'apriori_rules.xls' #结果文件
ap.find_rule(Data, support, confidence, ms).to_excel(outputfile) #联动

#检验
I1=Data['纺织服装_up'].values==1
I2=Data['综合_up'].values==1
I3=Data['轻工制造_up'].values==1
t123=np.zeros((1740))
t12=np.zeros((1740))
t123[I1&I2&I3]=1
t12[I1&I2]=1
sp1=sum(t123)/1740
co1=sum(t123)/sum(t12)

I1=Data['电气设备_up'].values==1
I2=Data['轻工制造_up'].values==1
t12=np.zeros((1740))
t1=np.zeros((1740))
t12[I1&I2]=1
t1[I1]=1
sp7=sum(t12)/1740
co7=sum(t12)/sum(t1)

print('co1= ',co1)
print('sp1= ',sp1)
print('co7= ',co7)
print('sp7= ',sp7)

import OneRule as OR
r=OR.rule(Data,0.3,0.59)


'''
#####行业轮动
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
        #取置信度大于0.59的关联规则
        if co>0.59:
           list1.append(c[k]+'--'+c[q])
           list2.append(sp)
           list3.append(co)
           
#定义字典，用于存放关联规则及其置信度、支持度   
R={'rule':list1,'support':list2,'confidence':list3}
#将字典转化为数据框
R=pd.DataFrame(R)
#将结果导出到Excel
R.to_excel('rule1.xlsx')
'''








