import pandas as pd
td=pd.read_excel('index300.xlsx')
A1=td['Idxtrd05'].values/pd.rolling_mean(td['Idxtrd05'].values,10)
A2=td['Idxtrd06'].values/pd.rolling_mean(td['Idxtrd06'].values,10)
A3=td['Idxtrd08'].values
A4=td['Idxtrd03'].values/pd.rolling_mean(td['Idxtrd05'].values,10)
A5=td['Idxtrd04'].values/pd.rolling_mean(td['Idxtrd05'].values,10)
A6=td['Idxtrd03'].values-td['Idxtrd04'].values
A7=td['Idxtrd05'].values-td['Idxtrd02'].values
X={'A1':A1,'A2':A2,'A3':A3,'A4':A4,'A5':A5,'A6':A6,'A7':A7}
X=pd.DataFrame(X)
X=X.iloc[9:-1,]

Y=td['Idxtrd05'].values[1:]-td['Idxtrd05'].values[:-1]
Y=Y[9:]
Y[Y>0]=1
Y[Y<=0]=-1
Y=Y.reshape(len(Y),1)

x_train=X.iloc[:len(X)-30,:]
Y_train=Y[:len(Y)-30]
x_test=X.iloc[len(X)-30:,:]
Y_test=Y[len(Y)-30:]

#支持向量机模型
from sklearn import svm
clf = svm.SVC(kernel='rbf')  
clf.fit(x_train, Y_train) 
rv1=clf.score(x_train, Y_train);
R=clf.predict(x_test)
R=R.reshape(len(R),1)
Z=R-Y_test
Rs1=len(Z[Z==0])/len(Z)

#逻辑模型
from sklearn.linear_model import LogisticRegression as LR
lr = LR()   #创建逻辑回归模型类
lr.fit(x_train, Y_train) #训练数据
rv2=lr.score(x_train, Y_train); # 模型准确率（针对训练数据）
R=lr.predict(x_test)
R=R.reshape(len(R),1)
Z=R-Y_test
Rs2=len(Z[Z==0])/len(Z)

#神经网络模型
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5,2), random_state=1)
clf.fit(x_train, Y_train);
rv3=clf.score(x_train, Y_train)
R=clf.predict(x_test)
R=R.reshape(len(R),1)
Z=R-Y_test
Rs3=len(Z[Z==0])/len(Z)

print('支持向量机模型准确率：',rv1)
print('逻辑模型准确率：',rv2)
print('神经网络模型准确率：',rv3)
print('---------------------------------------------')
print('支持向量机模型预测准确率：',Rs1)
print('逻辑模型预测准确率：',Rs2)
print('神经网络模型预测准确率：',Rs3)



