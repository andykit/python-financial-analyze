import pandas as pd
import numpy as np
data=pd.read_excel('data1.xlsx')
data2=data.iloc[data['Accper'].values=='2014-12-31',[0,2,3,4,5,6,7,8,9]]
da=data2.as_matrix()
da=da[(da[:,8]<4)&(da[:,8]>-4),:]
da[:,8]=1-(da[:,8]-min(da[:,8]))/(max(da[:,8])-min(da[:,8]))
for i in np.arange(1,8):
    da=da[da[:,i]>0,:]
    da=da[da[:,i]<8*np.mean(da[:,i]),:]
       
da=da[da[:,6]>=0.06,:]
from sklearn.preprocessing import MinMaxScaler 
X=da[:,1:]
scaler = MinMaxScaler()
scaler.fit(X) 
X=scaler.transform(X) 
X[:,2]=1-X[:,2]
X[:,3]=1-X[:,3]
X[:,4]=1-X[:,4]
   

from sklearn.decomposition import PCA  
pca=PCA(n_components=0.95)      #累计贡献率为95%
Y=pca.fit_transform(X)           #满足累计贡献率为95%的主成分数据
gxl=pca.explained_variance_ratio_ ##贡献率

F=np.zeros((len(Y)))
for i in range(len(gxl)):
    f=Y[:,i]*gxl[i]
    F=F+f
      
Fs1=pd.Series(F,index=da[:,0])
Fscore1=Fs1.sort_values(ascending=False)   #降序，True为升序
   
co=pd.read_excel('TRD_Co.xlsx')
Co=pd.Series(co['Stknme'].values,index=co['Stkcd'].values)
Co1=Co[da[:,0]]
Fs2=pd.Series(F,index=Co1.values)
Fscore2=Fs2.sort_values(ascending=False)   #降序，True为升序

trd=pd.read_excel('trd_2015.xlsx')

r_list=[]
for i in range(20):
    code=Fscore1.index[i]
    dt=trd.iloc[trd.iloc[:,0].values==code,:]
    I1=dt['Trddt'].values>='2015-05-01'
    I2=dt['Trddt'].values<='2015-12-31'
    dtt=dt.iloc[I1&I2,:].sort_values('Trddt')
    if len(dtt)>1:
        p1=dtt.iloc[0,3]
        p2=dtt.iloc[len(dtt)-1,3]
        r_list.append((p2-p1)/p1)
   
r_total=sum(r_list)
 

