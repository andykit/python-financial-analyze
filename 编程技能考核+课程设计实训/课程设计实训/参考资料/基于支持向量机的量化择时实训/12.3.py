# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
x=pd.read_excel('date.xlsx')
list1=['2016-01-04']
list2=[]
for t in range(1,len(x)-1):
    p=x.iloc[t-1,[2]][0]
    q=x.iloc[t,[2]][0]
    if q<p:
        list1.append(x.iloc[t,[1]][0])
        list2.append(x.iloc[t-1,[1]][0])
list2.append('2017-12-29')

trd=pd.read_excel('data1.xlsx')
num=12
A1=[]
A2=[]
A3=[]
A4=[]
Y=[]
for i in range(len(list1)):
    I1=trd['交易日期'].values>=list1[i]
    I2=trd['交易日期'].values<=list2[i]
    I=I1&I2
    A1.append(max(trd.loc[I,'最高价'].values))
    A2.append(min(trd.loc[I,'最低价'].values))
    A3.append(sum(trd.loc[I,'成交额'].values))
    #计算周收益率，从第2周开始
    if i>0:
       p1=trd.loc[trd['交易日期'].values==list2[i-1],'收盘价'].values
       p2=trd.loc[trd['交易日期'].values==list2[i],'收盘价'].values
       A4.append(float((p2-p1)/p1))
    #计算决策变量Y，最后一周不算
    if i<len(list1)-1:
       p1=trd.loc[trd['交易日期'].values==list2[i],'收盘价'].values
       p2=trd.loc[trd['交易日期'].values==list2[i+1],'收盘价'].values
       if p2-p1>0:
          Y.append(1)
       else:
          Y.append(-1)
    
A8=pd.rolling_mean(np.array(A3),4)
a8=A8[3:-1]
a1=A1[3:-1]
a2=A2[3:-1]
a3=A3[3:-1]
a4=A4[2:-1]
a5=A4[1:-2]
a6=A4[0:-3]
a7=A3[2:-2]
y=Y[3:]
y=np.array(y).reshape(len(y),1)

D={'a1':a1,'a2':a2,'a3':a3,'a4':a4,'a5':a5,'a6':a6,'a7':a7,'a8':a8}
Data=pd.DataFrame(D)
data=Data.as_matrix()

x_train=data[:len(data)-num,:]
x_test=data[len(data)-num:,:]
Y_train=y[:len(y)-num]
Y_test=y[len(y)-num:]


#from sklearn.preprocessing import MinMaxScaler
#scaler = MinMaxScaler()
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train) 
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)


#支持向量机模型
#from sklearn.linear_model import LogisticRegression as LR
#clf = LR()   #创建逻辑回归模型类
from sklearn import svm
clf = svm.SVC(kernel='rbf')  
clf.fit(x_train, Y_train) 
rv1=clf.score(x_train, Y_train);
rv=clf.predict(x_train)
R=clf.predict(x_test)
R=R.reshape(len(R),1)
Z=R-Y_test
Rs1=len(Z[Z==0])/len(Z)


