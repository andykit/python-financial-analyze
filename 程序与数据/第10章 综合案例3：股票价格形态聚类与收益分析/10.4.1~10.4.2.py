# -*- coding: utf-8 -*-
import pandas as pd
import df
import matplotlib.pyplot as plt

data=pd.read_excel('DA.xlsx')
#提取满足日期条件的数据
I1=data['Trddt'].values>'2017-06-01'
I2=data['Trddt'].values<'2017-08-31'
I=I1&I2
data1=data.iloc[I,:]
#提取代码600000的收盘价
dt=data1.loc[data1['Stkcd']==600000,['Clsprc']]['Clsprc']
#收盘价序列的index重排，从0开始
dt=pd.Series(dt.values,index=range(len(dt)))
#调用关键点获取函数
keydata=df.get_keydata(dt,12)
#绘图
plt.plot(dt.index,dt.values)
plt.plot(keydata.index,keydata.values,'r*--')
T=df.get_tz(keydata)
print(T)



