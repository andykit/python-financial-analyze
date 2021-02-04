# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
trd=pd.read_excel('trd.xlsx')
c=trd['Stkcd'].value_counts()
code=list(c.index)
#动态计算需要q个figure，其中每个figure绘制4个子图，每个子图代表一个股票，在子
#初始值设置q=0
q=0
#循环对每一个股票绘制其图形
for i in range(20):
    #第i个股票代码的收盘价，记为p,并计算其移动平均价
    #并构造绘图的x,y值
    p=trd.loc[trd['Stkcd'].values==code[i],'Clsprc'].values
    avg_p=pd.rolling_mean(p,10)
    x1=np.arange(0,len(p))
    y1=p
    y2=avg_p[9:]
    x2=np.arange(9,len(p))
    
    #如果i与4整除，代表需要重新建一个figure（因为每个figure有4个子图）
    if i%4==0: 
        q=q+1                    
        plt.figure(q)               
        plt.figure(figsize=(8,6))      
    plt.subplot(2,2,i%4+1)
    plt.tight_layout() #用于设置图像外部边缘自动调整
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.savefig(str(q))

