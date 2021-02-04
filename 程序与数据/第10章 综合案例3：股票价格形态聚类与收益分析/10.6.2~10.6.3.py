# -*- coding: utf-8 -*-
def FR1(DA,t_trd1,t_trd2,num):
   #输入：
   #DA--2017年股票交易数据
   #t_trd1--聚类数据区间开始日期
   #t_trd2--聚类数据区间结束日期
   #num--基于总体规模与投资效率指标的综合评价方法提取样本个数
   #输出：
   #Data--形态特征数据
   #KeyData--关键价格点数据
   #KeyData_index--关键价格点对应序号
   import pandas as pd    
   import fun
   import df
   import numpy as np
   dta=pd.read_excel('ddata.xlsx')
   r=fun.Fr(dta,'2016')
   c=r[0]
   code=list(c.index[0:num])
   p=-1
   td=pd.read_excel('交易日历数据表.xlsx')
   I1=td['Clddt'].values>=t_trd1
   I2=td['Clddt'].values<=t_trd2
   I=I1&I2
   ddt=td.loc[I,['Clddt']]
   M=len(ddt)
   num=10 #10
   Data=np.zeros((len(code),num))
   KeyData=np.zeros((len(code),num+1))
   KeyData_index=np.zeros((len(code),num+1))
   for t in range(len(code)):
      data=DA.loc[DA.iloc[:,0].values==code[t],['Trddt','Clsprc']]
      I1=data['Trddt'].values>=t_trd1
      I2=data['Trddt'].values<=t_trd2
      I=I1&I2
      dt=data.loc[I,['Clsprc']]['Clsprc']
      if len(dt)==M:
          p=p+1
          dt=pd.Series(dt.values,index=range(len(dt)))
          keydata=df.get_keydata(dt,num)
          T=df.get_tz(keydata)
          y=keydata
          KeyData[p,0]=code[t]
          Data[p,0]=code[t]
          Data[p,1:]=T
          KeyData_index[p,0]=code[t]
          KeyData[p,1:]=(y.values-min(y.values))/(max(y.values)-min(y.values))
          KeyData_index[p,1:]=y.index
   Data=Data[0:p,:]
   KeyData=KeyData[0:p,:]
   KeyData_index=KeyData_index[0:p,:]
   return (Data,KeyData,KeyData_index)

def FR2(DA,Data,KeyData,KeyData_index,s_trd1,s_trd2,class_num):
   #输入：
   #DA--2017年股票交易数据
   #Data--形态特征数据
   #KeyData--关键价格点数据
   #KeyData_index--关键价格点对应序号
   #s_trd1--收益率计算持有期开始日期
   #s_trd2--收益率计算持有期结束日期
   #class_num--聚类个数
   #输出：
   #Data_c--形态特征数据+聚类结果列
   #KeyData_c--关键价格点数据+聚类结果列
   #KeyData_index_c--关键价格点对应序号+聚类结果列
   #D--每只股票代码、所属聚类类别、收益率组成的数据框
   #list_cr--每类股票的总收益
   import pandas as pd
   #from sklearn.cluster import KMeans
   import numpy as np
   import kmean
   #model = KMeans(n_clusters = class_num, random_state=0, max_iter = 10000) 
   #model.fit(Data[:,1:]) 
   #c=model.labels_ 
   c=kmean.K_mean(Data[:,1:],class_num)
   p=len(Data)
   KeyData_c=np.hstack((KeyData,c.reshape(p,1)))
   KeyData_index_c=np.hstack((KeyData_index,c.reshape(p,1)))
   Data_c=np.hstack((Data,c.reshape(p,1)))
   list_code=[]
   list_codec=[]
   list_r=[]
   list_cr=[]
   for t in range(class_num):
       code_t=KeyData_c[KeyData_c[:,len(KeyData_c[0,:])-1]==t,0]
       r_t=0
       count_t=0
       for i in range(len(code_t)):
          I1=DA['Trddt'].values>=s_trd1
          I2=DA['Trddt'].values<=s_trd2
          I3=DA['Stkcd'].values==code_t[i]
          I=I1&I2&I3
          dta=DA.iloc[I,[2]]['Clsprc'].values
          if len(dta)>1:
             r=(dta[len(dta)-1]-dta[0])/dta[0]
             list_code.append(code_t[i])
             list_codec.append(t)
             list_r.append(r)
             r_t=r_t+r
             count_t=count_t+1
       list_cr.append(r_t/count_t)
   D={'code':list_code,'codec':list_codec,'coder':list_r}
   D=pd.DataFrame(D)
   return (Data_c,KeyData_c,KeyData_index_c,D,list_cr)

####训练样本x,y的构建
import pandas as pd 
DA=pd.read_excel('DA.xlsx') 
R1=FR1(DA,'2017-05-01','2017-07-31',400)
R2=FR2(DA,R1[0],R1[1],R1[2],'2017-08-01','2017-08-31',20)
dt1=R2[0]
cr1=pd.Series(R2[4])

crr=cr1.sort_values(ascending=False)
cr=list(crr.index)
for i in range(len(crr)):
    if i<5:
      dt1[dt1[:,len(dt1[0,:])-1]==cr[i],len(dt1[0,:])-1]=1
dt1[dt1[:,len(dt1[0,:])-1]!=1,len(dt1[0,:])-1]=-1

R1=FR1(DA,'2017-06-01','2017-08-31',400)
R2=FR2(DA,R1[0],R1[1],R1[2],'2017-09-01','2017-09-30',20)
dt2=R2[0]
cr2=pd.Series(R2[4])

crr=cr2.sort_values(ascending=False)
cr=list(crr.index)
for i in range(len(crr)):
    if i<5:
      dt2[dt2[:,len(dt2[0,:])-1]==cr[i],len(dt2[0,:])-1]=1
dt2[dt2[:,len(dt2[0,:])-1]!=1,len(dt2[0,:])-1]=-1

import numpy as np    
dt=np.vstack((dt2,dt1)) 
x=dt[:,1:-1]   
y=dt[:,len(dt[0,:])-1] 

####测试样本x1的构建
R1=FR1(DA,'2017-07-01','2017-09-30',400)
dt3=R1[0]
x1=dt3[:,1:]

####基于支持向量机预测模型的量化投资策略设计
from sklearn import svm
clf = svm.SVC()
clf.fit(x, y) 
result=clf.predict(x1) 
code=dt3[result==1,0]
list_r=[]
for i in range(len(code)):
    I1=DA['Trddt'].values>='2017-10-01'
    I2=DA['Trddt'].values<='2017-10-31'
    I3=DA['Stkcd'].values==code[i]
    I=I1&I2&I3
    dta=DA.iloc[I,[2]]['Clsprc'].values
    if len(dta)>1:
        r=(dta[len(dta)-1]-dta[0])/dta[0]
        list_r.append(r)
total_r=sum(list_r)

####沪深300指数同期收益率的计算    
indx300=pd.read_excel('index300.xlsx')    
I1=indx300['Idxtrd01'].values>='2017-10-01'
I2=indx300['Idxtrd01'].values<='2017-10-31'
In=I1&I2
da=indx300.loc[In,'Idxtrd05'].values
index300_r=(da[len(da)-1]-da[0])/da[0]

