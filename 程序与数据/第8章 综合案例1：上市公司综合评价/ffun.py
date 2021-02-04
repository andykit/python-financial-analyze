# -*- coding: utf-8 -*-
def Fr2(data,year):
    #输入：
    #data--财务指标数据
    #year--排名年度
    #输出：
    #Fscore1--排名结果（股票代码形式）
    #Fscore2--排名结果（股票名称形式）
    import pandas as pd
    import numpy as np
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
    return(Fscore1,Fscore2)

