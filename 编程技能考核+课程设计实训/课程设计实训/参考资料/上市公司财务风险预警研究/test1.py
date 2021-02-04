# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

A=pd.read_excel('2018年财务指标数据.xlsx')
df=A.dropna()
df=df.set_index('Stkcd')

#1.区分ST公司和非ST公司
#ST公司,选出前四个指标中任意一个小于0的公司，然后添加到B1，并在B1添加列标为1
B1=[]
for i in range(len(df)):
    if df.iloc[i,0]<0 or df.iloc[i,1]<0 or df.iloc[i,2]<0 or df.iloc[i,3]<0:       
       B1.append(df.iloc[i,4:])
B1=pd.DataFrame(B1)
B1.insert(loc=14, column='y', value='1')


#非ST公司选出前四个指标都大于0的公司，然后添加到B，并在B添加列标为0
B=[]
for i in range(len(df)):
    if df.iloc[i,0]>0 and df.iloc[i,1]>0 and df.iloc[i,2]>0 and df.iloc[i,3]>0:       
       B.append(df.iloc[i,4:])
B=pd.DataFrame(B)
#随机取和B1一样行数的数据
B=B.sample(n=len(B1), replace=True,  random_state=10, axis=0)
B.insert(loc=14, column='y', value='0')

#合并B1和B,并提取出这些样本公司的代码
f0= pd.concat([B, B1], axis = 0)
B2=pd.DataFrame(f0.index)


## 0-1规范化
min_max_scaler = MinMaxScaler()
min_max_scaler.fit(f0.iloc[:,:14])
XZ=min_max_scaler.transform(f0.iloc[:,:14]) 
f1=pd.DataFrame(XZ)
#合并B2，f1和f0的y列
f = pd.concat([B2,f1,pd.DataFrame(np.array(f0.iloc[:,14]))], axis = 1)

#提取95%的主成分
from sklearn.decomposition import PCA
pca=PCA(n_components=0.95) 
pca.fit(f.iloc[:,1:15])#调用pca对象中的fit()方法，对待分析的数据进行拟合训练
Y=pca.transform(f.iloc[:,1:15])#调用pca对象中的transform()方法，返回提取的主成分
tzxl=pca.components_##返回特征向量   
tz=pca.explained_variance_#返回特征值          
gxl=pca.explained_variance_ratio_ #返回主成分方差百分比（贡献率）
Y=pd.DataFrame(Y)

#神经网络模型
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.neural_network import MLPClassifier
x=Y.iloc[:,:].as_matrix()#确定自变量
y=f.iloc[:,15].as_matrix()#确定因变量
#将样本随机划分为4:1的训练样本和验证样本
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=1)
#根据q=√(n+m)+a确定隐含层，经测试隐含层在18的样本准确率最高
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=12, random_state=1)
clf.fit(x_train, y_train)#调用clf对象中的fit()方法进行网络训练。
rv=clf.score(x_train, y_train)#调用clf对象中的score ()方法，获得神经网络的预测准确率（针对训练数据）
r=clf.predict(x_train)#得出训练集的预测结果
R=clf.predict(x_test)#得出测试集的预测结果


# 统计训练样本实际ST和非ST的个数
y_train=pd.DataFrame(y_train)
a1=0
a0=0
for i in range(len(y_train)):
    if int(y_train.iloc[i,0])==1:
        a1=a1+1
    else:
        a0=a0+1
        
#统计训练样本预测的ST和非ST的个数  
r=pd.DataFrame(r)
b1=0
b0=0
for i in range(len(r)):
    if int(r.iloc[i,0])==1:
        b1=b1+1
    else:
        b0=b0+1 
        
#统计检验样本实际的ST和非ST的个数         
y_test=pd.DataFrame(y_test)
c1=0
c0=0
for i in range(len(y_test)):
    if int(y_test.iloc[i,0])==1:
        c1=c1+1
    else:
        c0=c0+1 

#统计检验样本预测的ST和非ST的个数  
R=pd.DataFrame(R)
d1=0
d0=0
for i in range(len(R)):
    if int(R.iloc[i,0])==1:
        d1=d1+1
    else:
        d0=d0+1 

#计算测试样本的准确率 ，用预测正确个数和总个数计算出检测样本准确率
e=0
e1=0     
for i in range(len(R)):
    if R.iloc[i,0]==y_test.iloc[i,0]:
        e=e+1
    else:
        e1=e+1
Rs=e/len(R)
print('模型预测的准确率为',rv)  
print('预测的准确率为',Rs)       









