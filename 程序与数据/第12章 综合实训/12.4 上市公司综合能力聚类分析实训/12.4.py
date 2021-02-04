# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
#1.数据预处理，即清洗掉<0，nan,异常值，标准化
dta=pd.read_excel('data.xlsx')
dta=dta[dta>0]
dta=dta.dropna()
dta=dta.iloc[:,[0,2,3,4,5,6,7,8,9,10,11]]
data2=dta.as_matrix()
for i in range(1,11):
    data2=data2[data2[:,i]<8*np.mean(data2[:,i]),:]

X=data2[:,1:]
from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()
scaler.fit(X) 
X=scaler.transform(X)

#2.K-均值聚类分析
from sklearn.cluster import KMeans   
model = KMeans(n_clusters = 5, random_state=0, max_iter = 1000) 
model.fit(X) 
c=model.labels_
Fs=pd.Series(c,index=data2[:,0])
Fs=Fs.sort_values(ascending=True)

trd=pd.read_excel('trd.xlsx')
R=[]
for i in range(5):
    Fs_i=Fs[Fs==i]
    code_i=list(Fs_i.index)
    r_i=0
    for t in range(len(code_i)):
        rd=trd.loc[trd['Stkcd'].values==code_i[t],['Trddt','Adjprcwd']]
        rd=rd.sort_values('Trddt')
        p=rd['Adjprcwd'].values
        if len(p)>0:
           p1=p[0]
           p2=p[len(p)-1]
           r=(p2-p1)/p1
           r_i=r_i+r
    R.append(r_i)
