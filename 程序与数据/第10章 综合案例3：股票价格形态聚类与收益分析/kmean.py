def K_mean(data,knum):
    #输入：data--聚类特征数据集，要求为数据结构要求为numpy数值数组
    #输入：knum--聚类个数
    #返回值，data后面加一列类别，显示类别
    import pandas as pd
    import numpy as np
    p=len(data[0,:])                  #聚类数据维度
    cluscenter=np.zeros((knum,p))     #定预定义元素为全0的初始聚类中心
    lastcluscenter=np.zeros((knum,p)) #定预定义元素为全0的旧聚类中心
    #初始聚类中心和旧聚类中心初始化，取数据的前knum行作为初始值
    ss=pd.DataFrame(data)
    ss=ss.drop_duplicates()
    ss=ss.as_matrix()
    
    for i in range(knum):
      cluscenter[i,:]=ss[i,:]
      lastcluscenter[i,:]=ss[i,:]
      
    #预定义聚类类别一维数组，用于存放每次计算样本的所属类别
    clusindex=np.zeros((len(data)))
    count=0
    while 1:
        count=count+1
        for i in range(len(data)):
              #计算第i个样本到各个聚类中心的欧式距离
              #预定义sumsquare，用于存放第i个样本到各个聚类中心的欧式距离
              sumsquare=np.zeros((knum))
              for k in range(knum):
                   s=data[i,:]-cluscenter[k,:]
                   sumsquare[k]=len(s[s!=0])
              #    sumsquare[k]=sum((data[i,:]-cluscenter[k,:])**2)
              #sumsquare=np.sqrt(sumsquare)
              #第i个样本到各个聚类中心的欧式距离进行升序排序
              s=pd.Series(sumsquare).sort_values()
              #判断第i个样本的类归属（距离最小，即s序列中第0个位置的index）
              clusindex[i]=s.index[0]
              
        #将聚类结果添加到聚类数据最后一列
        clusdata=np.hstack((data,clusindex.reshape((len(data),1))))
        #更新聚类中心，新的聚类中心为对应类别样本特征的均值
        for i in range(knum):
            ci=clusdata[clusdata[:,p]==i,:-1]
            for j in range(p):
                s1=pd.Series(ci[:,j]).value_counts()
                cluscenter[i,j] =s1.index[0]
              #cluscenter[i,:]=np.mean(clusdata[clusdata[:,p]==i,:-1],0).reshape(1,p)
      
        #新的聚类中心与旧的聚类中心相减
        t=abs(lastcluscenter-cluscenter)
        #如果新的聚类中心与旧的聚类中心一致，即聚类中心不发生变化，返回聚类结果，并退出循环
        if sum(sum(t))==0:    
            return clusdata[:,p]
            break
        #如果更新的聚类中心与旧的聚类中心不一致，将更新的聚类中心赋给旧的聚类中心，进入下一次循环
        else:
            for k in range(knum):
                lastcluscenter[k,:]=cluscenter[k,:]  
        if count==10000:
            return clusdata[:,p]
            break
      
