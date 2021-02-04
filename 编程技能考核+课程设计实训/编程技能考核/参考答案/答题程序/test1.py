import pandas as pd
import numpy as np
import math
data=pd.read_excel('附件一：已结束项目任务数据.xls')
trd=pd.read_excel('附件二：会员信息数据.xlsx')
x1=data.loc[data['任务号码'].values=='A0001','任务gps纬度'].values#第A0020任务的纬度
y1=data.loc[data['任务号码'].values=='A0001','任务gps经度'].values
x2=data.loc[data['任务号码'].values=='A0002','任务gps纬度'].values#第A0020任务的纬度
y2=data.loc[data['任务号码'].values=='A0002','任务gps经度'].values#第A0020任务的经度
b=trd.iloc[:,[1]].values
z1=trd.iloc[:,0].values
x4=[]#第g个会员的纬度
y4=[]#第g个会员的经度
for g in range(len(b)):
    q=str(b[g])
    l=q.find(' ',0,len(q))
    d1=float(q[2:l])
    d2=float(q[l:len(q)-2])
    x4.append(d1)
    y4.append(d2)
D1=np.zeros(len(x4))
D2=np.zeros(len(x4))
for i in range(len(x4)):
    d1=111.199*math.sqrt((x1-x4[i])**2+(y1-y4[i])**2*math.cos((x1+x4[i])*math.pi/180)**2)
    D1[i]=d1
    d2=111.199*math.sqrt((x2-x4[i])**2+(y2-y4[i])**2*math.cos((x2+x4[i])*math.pi/180)**2)
    D2[i]=d2
s_A0001=pd.Series(D1,index=z1)#会员之间的距离
s_A0002=pd.Series(D2,index=z1)
A0001_Bnum=len(D1[D1<=5])
D3=s_A0002[s_A0002<=5]
list3=list(D3.index)
A0001_Bavg=0
for j in range(len(list3)):
    xy=trd.loc[trd['会员编号'].values==list3[j],'信誉值'].values
    A0001_Bavg=A0001_Bavg+xy