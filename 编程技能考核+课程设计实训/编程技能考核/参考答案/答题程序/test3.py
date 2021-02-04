import pandas as pd
data=pd.read_excel('高教数据.xlsx')
X=data.iloc[:,1:]
from sklearn.preprocessing import StandardScaler#规范化处理
scaler = StandardScaler()
scaler.fit(X) 
X=scaler.transform(X)
from sklearn.decomposition import PCA#主成分分析模块
pca=PCA(n_components=0.90) #累计贡献率达到95%以上
pca.fit(X)
Y=pca.transform(X)#主成分
from sklearn.cluster import KMeans  #K-均值聚类模块 
model = KMeans(n_clusters = 4, random_state=0, max_iter = 500) 
model.fit(Y) 
c=model.labels_#K-均值聚类结果
Fs=pd.Series(c,index=data['地区'])
Fs=Fs.sort_values(ascending=True)#K-均值聚类整理后结果
print('第0类为：',list(Fs[Fs==0].index))
print('第1类为：',list(Fs[Fs==1].index))
print('第2类为：',list(Fs[Fs==2].index))
print('第3类为：',list(Fs[Fs==3].index))
