import pandas as pd
import numpy as np
td=pd.read_excel('沪深300指数2014年交易数据.xlsx')
#1、获取指标
A1=td['Idxtrd05'].values/pd.rolling_mean(td['Idxtrd05'].values,10)
A2=td['Idxtrd06'].values/pd.rolling_mean(td['Idxtrd06'].values,10)
A4=td['Idxtrd03'].values/pd.rolling_mean(td['Idxtrd05'].values,10)
A5=td['Idxtrd04'].values/pd.rolling_mean(td['Idxtrd05'].values,10)
A6=td['Idxtrd03'].values-td['Idxtrd04'].values
A7=td['Idxtrd05'].values-td['Idxtrd02'].values
Y=td['Idxtrd05'].values[1:]-td['Idxtrd05'].values[:-1]
A3=np.zeros(len(td))
for i in range(len(td)):
    if i>0:
       A3[i]=(td.loc[i,'Idxtrd05']-td.loc[i-1,'Idxtrd05'])/td.loc[i-1,'Idxtrd05']   
X={'A1':A1,'A2':A2,'A3':A3,'A4':A4,'A5':A5,'A6':A6,'A7':A7}
X=pd.DataFrame(X)
X=X.iloc[9:,]
#对指标A1~A7作标准化处理
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X) 
X=scaler.transform(X)
X=pd.DataFrame(X)
Y=Y[8:]
Y[Y>0]=1
Y[Y<=0]=-1
Y=Y.reshape(len(Y),1)
Y=pd.DataFrame(Y)
x = X.iloc[:len(X)-30,:].as_matrix()
y = Y.iloc[:len(Y)-30,:].as_matrix()
x1= X.iloc[len(X)-30:,:].as_matrix()
y1= Y.iloc[len(Y)-30:].as_matrix()
#2、支持向量机
from sklearn import svm
clf = svm.SVC(kernel='rbf')
clf.fit(x, y)
score=clf.score(x, y); # 模型准确率（针对训练数据）
R2=clf.predict(x1)
Z=R2-y1
Z=Z[:,0]
Rv=len(Z[Z==0])/len(Z) #预测准确率
print('模型准确率为：',score)
print('预测准确率为：',Rv)
