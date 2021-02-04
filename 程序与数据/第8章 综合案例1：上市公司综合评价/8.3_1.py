# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 20:53:57 2018

@author: Administrator
"""
import pandas as pd
data=pd.read_excel('data.xlsx')
data2=data.iloc[data['Accper'].values=='2016-12-31',[ 0,2,3,4,5,6,7,8,9,10,11]]
data2=data2[data2>0]
data2=data2.dropna()
from sklearn.preprocessing import StandardScaler  
X=data2.iloc[:,1:]
scaler = StandardScaler()
scaler.fit(X) 
X=scaler.transform(X)  
from sklearn.decomposition import PCA 
pca=PCA(n_components=0.95)      #累计贡献率为95%
Y=pca.fit_transform(X)            #满足累计贡献率为95%的主成分数据
gxl=pca.explained_variance_ratio_   #贡献率
import numpy as np
F=np.zeros((len(Y)))
for i in range(len(gxl)):
    f=Y[:,i]*gxl[i]
    F=F+f
    
fs1=pd.Series(F,index=data2['Stkcd'].values)
Fscore1=fs1.sort_values(ascending=False)   #降序，True为升序
    
co=pd.read_excel('TRD_Co.xlsx')
Co=pd.Series(co['Stknme'].values,index=co['Stkcd'].values)
Co1=Co[data2['Stkcd'].values]
fs2=pd.Series(F,index=Co1.values)
Fscore2=fs2.sort_values(ascending=False)   #降序，True为升序

trd=pd.read_excel('trd_'+str(2017)+'.xlsx')
r_list=[]
for i in range(30):
    code=Fscore1.index[i]
    dt=trd.iloc[trd.iloc[:,0].values==code,:]
    I1=dt['Trddt'].values>='2017-05-01'
    I2=dt['Trddt'].values<='2017-12-31'
    dtt=dt.iloc[I1&I2,:].sort_values('Trddt')
    if len(dtt)>1:
        p1=dtt.iloc[0,3]
        p2=dtt.iloc[len(dtt)-1,3]
        r_list.append((p2-p1)/p1)
   
r_total=sum(r_list)

