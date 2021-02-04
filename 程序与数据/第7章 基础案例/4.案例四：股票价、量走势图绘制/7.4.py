# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_excel('trd.xlsx')
dt=data.loc[data['股票代码']==600000,['交易日期','收盘价','交易量']]
I1=dt['交易日期'].values>='2017-01-03'
I2=dt['交易日期'].values<='2017-01-20'
dta=dt.iloc[I1&I2,:]
y1=dta['收盘价']
x1=range(len(y1))
I3=dt['交易日期'].values>='2017-01-03'
I4=dt['交易日期'].values<='2017-01-24'
dta=dt.iloc[I3&I4,:]
y2=dta['交易量']
x2=range(len(y2))

D=np.zeros((11))
list1=list()
for m in range(11):
    m=m+1
    if m<10:
        m1='2017-0'+str(m)+'-01'
        m2='2017-0'+str(m)+'-31'
        mon='0'+str(m)
    else:
        m1='2017-'+str(m)+'-01'
        m2='2017-'+str(m)+'-31'
        mon=str(m)
    I1=dt['交易日期'].values>=m1
    I2=dt['交易日期'].values<=m2
    D[m-1]=dt.iloc[I1&I2,[2]].sum()[0]
    list1.append(mon)

plt.figure(1)
plt.plot(x1,y1)
plt.xlabel(u'日期',fontproperties='SimHei')
plt.ylabel(u'收盘价',fontproperties='SimHei')
plt.title(u'收盘价走势图',fontproperties='SimHei')
plt.savefig('1')

plt.figure(2)
plt.bar(x2,y2)
plt.xlabel(u'日期',fontproperties='SimHei')
plt.ylabel(u'交易量 ',fontproperties='SimHei')
plt.title(u'交易量趋势图',fontproperties='SimHei')
plt.savefig('2')

plt.figure(3)
plt.pie(D,labels=list1,autopct='%1.2f%%') #保留小数点后两位
plt.title(u'月交易量分布图',fontproperties='SimHei')
plt.savefig('3')

plt.figure(4)
plt.figure(figsize=(14,6))
plt.subplot(1,3,1)
plt.plot(x1,y1)
plt.xlabel(u'日期',fontproperties='SimHei')
plt.ylabel(u'收盘价',fontproperties='SimHei')
plt.title(u'收盘价走势图',fontproperties='SimHei')
plt.subplot(1,3,2)
plt.bar(x2,y2)
plt.xlabel(u'日期',fontproperties='SimHei')
plt.ylabel(u'交易量',fontproperties='SimHei')
plt.title(u'交易量趋势图',fontproperties='SimHei')
plt.subplot(1,3,3)
plt.pie(D,labels=list1,autopct='%1.2f%%') #保留小数点后两位
plt.title(u'月交易量分布图',fontproperties='SimHei')
plt.savefig('4')


