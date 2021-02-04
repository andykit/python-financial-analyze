
import pandas as pd
import numpy as np
data=pd.read_excel('财务指标数据.xlsx')
data2=data.iloc[:,[ 0,2,3,4,5,6,7,8,9]]
data2=data2[data2>0]
data2=data2.dropna()
data2=data2.as_matrix()
for i in range(1,9):
    data2=data2[data2[:,i]<8*np.mean(data2[:,i]),:]
    
dta=pd.read_excel('申万行业分类.xlsx')
stkcd=dta.loc[dta['行业名称'].values=='计算机','股票代码'].values
s=data2[:,0]
I=s==stkcd[0]
for i in range(1,len(stkcd)):
    I1=s==stkcd[i]
    I=I|I1
ddata=data2[I,:]
X=ddata[:,1:]

from sklearn.preprocessing import MinMaxScaler
scaler =  MinMaxScaler()
scaler.fit(X) 
X=scaler.transform(X) 

from sklearn.decomposition import PCA 
pca=PCA(n_components=0.95)      #累计贡献率为95%
Y=pca.fit_transform(X) 
tzxl=pca.components_              #返回特征向量
tz=pca.explained_variance_          #返回特征值
gxl=pca.explained_variance_ratio_    #返回主成分方差百分比（贡献率）

scaler =  MinMaxScaler()
scaler.fit(Y) 
Y=scaler.transform(Y) 


from sklearn.cluster import KMeans   
model = KMeans(n_clusters = 5, random_state=0, max_iter = 1000) 
model.fit(Y) 
c=model.labels_
center=model.cluster_centers_
center=pd.DataFrame(center)
center.columns=['Y1','Y2','Y3']

Fs=pd.Series(c,index=ddata[:,0])
Fs=Fs.sort_values()
co=pd.read_excel('公司基本信息表.xlsx')
co1=pd.Series(co['Stknme'].values,index=co['Stkcd'].values)
for i in range(5):
    q=co1[Fs[Fs==i].index]
    q=pd.DataFrame(q)
    q.to_excel('c'+str(i)+'.xlsx')

rd=pd.read_excel('利润数据.xlsx')
r_c=[]
for n in range(5):
    cn=list(Fs[Fs==n].index)
    r1_n=0
    r2_n=0
    for t in cn:
        I1=rd['Accper'].values=='2014-12-31'
        I2=rd['Accper'].values=='2015-12-31'
        I3=rd['Stkcd'].values==t
        index1=I1&I3
        index2=I2&I3
        r1=rd.loc[index1,'B002000101'].values
        r2=rd.loc[index2,'B002000101'].values
        if len(r1)>0:
           r1_n=r1_n+r1
        if len(r2)>0:
           r2_n=r2_n+r2
    p2=r2_n/len(cn)
    p1=r1_n/len(cn)
    r_c.append((p2-p1)/p1)

r_c=np.array(r_c)
dt=np.hstack((center.values,r_c))
dtt=pd.DataFrame(dt)
dtt.columns=['Y1','Y2','Y3','r_c']

