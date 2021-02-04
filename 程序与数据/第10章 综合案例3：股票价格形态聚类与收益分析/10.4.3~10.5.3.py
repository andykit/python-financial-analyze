import pandas as pd  
import fun
dta=pd.read_excel('ddata.xlsx')
r=fun.Fr(dta,'2016')
c=r[0][0:400]
cn=r[1][0:400]
code=list(c.index) 

td=pd.read_excel('交易日历数据表.xlsx')
I1=td['Clddt'].values>'2017-05-01'
I2=td['Clddt'].values<'2017-07-30'
I=I1&I2
ddt=td.loc[I,['Clddt']]
M=len(ddt)

import df
import numpy as np
num=13
p=-1
DA=pd.read_excel('DA.xlsx') 
#预定义股票价格走势特征化数据，第0列为股票代码，其余为特征化数据（num-1个）
Data=np.zeros((len(code),num))
#预定义股票价格走势关键点数据，第0列为股票代码，其余为关键点数据（num个）
KeyData=np.zeros((len(code),num+1))
#预定义股票价格走势关键点下标，第0列为股票代码，其余为关键点下标（num个）
KeyData_index=np.zeros((len(code),num+1))
#对每一个股票代码，提取其关键点数据、计算其特征化数据，同时对关键点数据标准化处#理（极差法）
for t in range(len(code)):
    data=DA.loc[DA.iloc[:,0].values==code[t],['Trddt','Clsprc']]
    I1=data['Trddt'].values>'2017-05-01'
    I2=data['Trddt'].values<'2017-07-30'
    I=I1&I2
    #提取第t个股票代码的价格数据，同时下标重排，从0开始
    dt=data.loc[I,['Clsprc']]['Clsprc']
    dt=pd.Series(dt.values,index=range(len(dt)))
    if len(dt)==M:
        p=p+1
        keydata=df.get_keydata(dt,num)
        T=df.get_tz(keydata)
        y=keydata
        KeyData[p,0]=code[t]
        Data[p,0]=code[t]
        Data[p,1:]=T
        KeyData_index[p,0]=code[t]
        KeyData[p,1:]=(y.values-min(y.values))/(max(y.values)-min(y.values))
        KeyData_index[p,1:]=y.index
Data=Data[0:p,:]
KeyData=KeyData[0:p,:]
KeyData_index=KeyData_index[0:p,:]

from sklearn.cluster import KMeans
model = KMeans(n_clusters = 20, random_state=0, max_iter = 10000) 
model.fit(Data[:,1:]) 
c=model.labels_ 
KeyData_c=np.hstack((KeyData,c.reshape(p,1)))
KeyData_index_c=np.hstack((KeyData_index,c.reshape(p,1)))
Data_c=np.hstack((Data,c.reshape(p,1)))

   
list_code=[]
list_codec=[]
list_r=[]
list_cr=[]
for t in range(20):
    code_t=KeyData_c[KeyData_c[:,len(KeyData_c[0,:])-1]==t,0]
    r_t=0
    count_t=0
    for i in range(len(code_t)):
        I1=DA['Trddt'].values>'2017-08-01'
        I2=DA['Trddt'].values<'2017-08-30'
        I3=DA['Stkcd'].values==code_t[i]
        I=I1&I2&I3
        dta=DA.iloc[I,[2]]['Clsprc'].values
        if len(dta)>1:
           r=(dta[len(dta)-1]-dta[0])/dta[0]
           list_code.append(code_t[i])
           list_codec.append(t)
           list_r.append(r)
           r_t=r_t+r
           count_t=count_t+1
    list_cr.append(r_t/count_t)
D={'股票代码':list_code,'类别':list_codec,'收益率':list_r}
D=pd.DataFrame(D)

import matplotlib.pyplot as plt
p=0
for t in range(20):
    dat1=KeyData_c[KeyData_c[:,len(KeyData_c[0,:])-1]==t,1:-1]
    dat2=KeyData_index_c[KeyData_index_c[:,len(KeyData_index_c[0,:])-1]==t,1:-1]
    if t%4==0: 
        p=p+1
        plt.figure(p)
        plt.figure(figsize=(8,6))
        
    plt.subplot(2,2,t%4+1)
    plt.title(u'一个月后平均收益率为：'+str(list_cr[t]),fontproperties='SimHei',size=10)
    plt.tight_layout()
    for k in range(5):
        if k<len(dat1):
           plt.plot(dat2[k,:],dat1[k,:])
    plt.savefig(str(p))

