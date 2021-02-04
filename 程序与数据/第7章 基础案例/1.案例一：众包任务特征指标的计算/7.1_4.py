# -*- coding: utf-8 -*-
import pandas as pd     #导入pandas库
import numpy as np      #导入nmypy库
import math             #导入数学函数模
A=pd.read_excel('附件一：已结束项目任务数据.xls') 
B=pd.read_excel('附件二：会员信息数据.xlsx')
# 预定义，存放所有任务的指标Z1、Z2、Z3、Z4、Z5
Z=np.zeros((len(A),5))
for q in range(len(A)):
    A_Wq=A.iloc[q,1]  #第q个任务的维度
    A_Jq=A.iloc[q,2]  #第q个任务的经度
    # 预定义数组D1，用于存放第q个任务与所有任务之间的距离
    # 预定义数组D2，用于存放第q个任务与所有会员之间的距离
    D1=np.zeros((len(A)))
    D2=np.zeros((len(B)))
    for t in range(len(A)):
       A_Wt=A.iloc[t,1]  #第t个任务的维度
       A_Jt=A.iloc[t,2]  #第t个任务的经度

       #第q个任务到第t个任务之间的距离
       dt=111.19*math.sqrt((A_Wq-A_Wt)**2+(A_Jq-A_Jt)**2*
          math.cos((A_Wq+A_Wt)*math.pi/180)**2);  
       D1[t]=dt
    for k in range(len(B)):
       B_WJ=B.iloc[k,1]
       I=B_WJ.find(' ',0,len(B_WJ))
       B_Wk=float(B_WJ[0:I])          #第k个会员的维度
       B_Jk=float(B_WJ[I:len(B_WJ)])  #第k个会员的经度
       #第q个任务到第k个会员之间的距离
       dk=111.19*math.sqrt((A_Wq-B_Wk)**2+(A_Jq-B_Jk)**2*
          math.cos((A_Wq+B_Wk)*math.pi/180)**2); 
       D2[k]=dk

    Z1=len(D1[D1<=5]) 
    Z2=A.iloc[D1<=5,[3]].mean()[0]
    Z3=len(D2[D2<=5])     
    Z4=B.iloc[D2<=5,[2,4]].sum()[0]
    Z5=B.iloc[D2<=5,[2,4]].sum()[1]/Z3
    Z[q,0]=Z1
    Z[q,1]=Z2
    Z[q,2]=Z3
    Z[q,3]=Z4
    Z[q,4]=Z5


