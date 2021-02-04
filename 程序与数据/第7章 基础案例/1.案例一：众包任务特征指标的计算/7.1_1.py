# -*- coding: utf-8 -*-
import pandas as pd     #导入pandas库
import math             #导入数学函数模
A=pd.read_excel('附件一：已结束项目任务数据.xls') 
B=pd.read_excel('附件二：会员信息数据.xlsx')
A_W0=A.iloc[0,1]  #第0个任务的维度
A_J0=A.iloc[0,2]  #第0个任务的经度
A_W1=A.iloc[1,1]  #第1个任务的维度
A_J1=A.iloc[1,2]  #第1个任务的经度

B_WJ=B.iloc[0,1]
I=B_WJ.find(' ',0,len(B_WJ))
B_W0=float(B_WJ[0:I])          #第0个会员的维度
B_J0=float(B_WJ[I:len(B_WJ)])  #第0个会员的经度

#第0个任务到第1个任务之间的距离
d1=111.19*math.sqrt((A_W0-A_W1)**2+(A_J0-A_J1)**2*math.cos((A_W0+A_W1)*math.pi/180)**2);  

#第0个任务到第0个会员之间的距离
d2=111.19*math.sqrt((A_W0-B_W0)**2+(A_J0-B_J0)**2*math.cos((A_W0+B_W0)*math.pi/180)**2);
print('d1= ',d1)
print('d2= ',d2)


