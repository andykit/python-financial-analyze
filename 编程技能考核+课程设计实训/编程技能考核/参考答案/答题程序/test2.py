import pandas as pd
import numpy as np
data=pd.read_excel('银行贷款审批数据.xlsx')
d1=data.iloc[:,0:6]
from sklearn.preprocessing import Imputer 
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(d1)
d1=imp.transform(d1)
d2=data.iloc[:,6:15]
imp = Imputer(missing_values='NaN', strategy='median', axis=1)
imp.fit(d2)
d2=imp.transform(d2)
from sklearn.preprocessing import StandardScaler
X=d1
scaler = StandardScaler()
scaler.fit(X) 
X=scaler.transform(X)
D=np.zeros((len(d2),15))
for j in range(6):
    D[:,j]=X[:,j]
for i in range(9):
    D[:,i+6]=d2[:,i]
x = D[:600,:]
y = data.iloc[:600,15].as_matrix()
x1= D[600:,:]
y1= data.iloc[600:,15].as_matrix()
from sklearn import svm#支持向量机模型
clf = svm.SVC(kernel='rbf')  
clf.fit(x, y) 
rv=clf.score(x, y);
R1=clf.predict(x1)
Z=R1-y1
Rs1=len(Z[Z==0])/len(Z)
from sklearn.linear_model import LogisticRegression as LR#逻辑回归模型
lr = LR()   #创建逻辑回归模型类
lr.fit(x, y) #训练数据
r=lr.score(x, y); # 模型准确率（针对训练数据）
R2=lr.predict(x1)
Z=R2-y1
Rs2=len(Z[Z==0])/len(Z)
from sklearn.neural_network import MLPClassifier#神经网络模型
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5,2), random_state=1)
clf.fit(x, y);
rv=clf.score(x,y)
R3=clf.predict(x1)
Z=R3-y1
Rs3=len(Z[Z==0])/len(Z)
print('支持向量机模型预测结果为：',R1)
print('逻辑回归模型预测结果为：',R2)
print('神经网络模型预测结果为：',R3)
print('支持向量机模型预测精度为：',Rs1)
print('逻辑回归模型预测精度为：',Rs2)
print('神经网络模型预测精度为：',Rs3)
hz=['支持向量机','逻辑回归','神经网络']
zz=[Rs1,Rs2,Rs3]
import matplotlib.pyplot as plt 
plt.figure(1)
font={'family':'SimHei'}
plt.rc('font',**font)
plt.bar(hz,zz)


