import Ind
import pandas as pd
data=pd.read_excel('data.xlsx')
MA= Ind.MA(data,5,10,20) 
macd=Ind.MACD(data)
kdj=Ind.KDJ(data,9)
rsi6=Ind.RSI(data,6)
rsi12=Ind.RSI(data,12)
rsi24=Ind.RSI(data,24)
bias5=Ind.BIAS(data,5)
bias10=Ind.BIAS(data,10)
bias20=Ind.BIAS(data,20)
obv=Ind.OBV(data) 
y=Ind.cla(data)

#将计算出的技术指标与交易日期以及股价的涨跌趋势利用字典整合在一起
pm={'交易日期':data['Trddt'].values}
PM=pd.DataFrame(pm)
DF={'MA5':MA[0],'MA10':MA[1],'MA20':MA[2],'MACD':macd,
    'K':kdj[0],'D':kdj[1],'J':kdj[2],'RSI6':rsi6,'RSI12':rsi12,
    'RSI24':rsi24,'BIAS5':bias5,'BIAS10':bias10,'BIAS20':bias20,'OBV':obv}
DF=pd.DataFrame(DF)
s1=PM.join(DF)

y1={'涨跌趋势':y}
ZZ=pd.DataFrame(y1)
s2=s1.join(ZZ)

#去掉空值
ss=s2.dropna()
#将ss中第6列不为0的值提取出来，存放到Data中
Data=ss[ss.iloc[:,6].values!=0]

 #提取训练和预测数据
x1=Data['交易日期']>='2017-01-01'
x2=Data['交易日期']<='2017-11-30'
xx=x1&x2
index=xx.values==True
index1=xx.values==False
x_train=Data.iloc[index,1:15]  
y_train=Data.iloc[index,[15]]
x_test=Data.iloc[index1,1:15]
y_test=Data.iloc[index1,[15]]


#数据标准化
from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()
scaler.fit(x_train) 
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test) 


from sklearn.linear_model import LogisticRegression as LR
clf = LR()
clf.fit(x_train, y_train) 
result=clf.predict(x_test)
sc=clf.score(x_train, y_train)
'''
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=8, random_state=1)
     # 多个隐含层hidden_layer_sizes(5,2)
clf.fit(x_train, y_train) 
result=clf.predict(x_test)
sc=clf.score(x_train, y_train)

from sklearn import svm
clf = svm.SVC()
clf.fit(x_train, y_train) 
result=clf.predict(x_test)
sc=clf.score(x_train, y_train)
'''
result=pd.DataFrame(result)
#提取预测样本的交易日期
ff=Data.iloc[index1,0]
#将预测结果与实践结果整合在一起，进行比较
pm1={'交易日期':ff.values,'预测结果':result.iloc[:,0].values,'实际结果':y_test.iloc[:,0].values}
result1=pd.DataFrame(pm1)
z=result1['预测结果'].values-result1['实际结果'].values
R=len(z[z==0])/len(z)

r_list=[]
r_trd=[]
for t in range(len(result1)-1):
    if result1['预测结果'].values[t]==1:
        p1=data.loc[data['Trddt'].values== result1['交易日期'].values[t],'Clsprc'].values
        dt=data.loc[data['Trddt'].values>result1['交易日期'].values[t],['Trddt','Clsprc']]
        dt=dt.sort_values('Trddt')
        p2=dt['Clsprc'].values[0]
        r=(p2-p1)/p1
        r_list.append(r)
        r_trd.append(result1['交易日期'].values[t])
r_total=sum(r_list)
trd_r={'交易日期':r_trd,'收益率':r_list}
trd_r=pd.DataFrame(trd_r)

