def Fr(data,year):
    import pandas as pd
    data2=data.iloc[data['Accper'].values==str(year)+'-12-31',[ 0,2,3,4,5,6,7,8,9,10,11]]
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
    return (Fscore1,Fscore2)
