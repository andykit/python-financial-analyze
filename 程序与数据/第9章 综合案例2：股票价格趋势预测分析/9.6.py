import pandas as pd    
import fun
import Re_comput
dt=pd.read_excel('ddata.xlsx')  
r=fun.Fr(dt,'2016')
c=r[0]
code=list(c.index[0:20])  

DA=pd.read_excel('DA.xlsx')   #2017年所有上市股票交易数据

list_code=[]
list_00=[]
list_01=[]
list_02=[]
list_10=[]
list_11=[]
list_12=[]
list_20=[]
list_21=[]
list_22=[]

for i in range(len(code)):
   data=DA.iloc[DA.iloc[:,0].values==code[i],:]
   if len(data)>1:
       list_code.append(code[i])
       z0=Re_comput.Re(data,0)
       z1=Re_comput.Re(data,1)
       z2=Re_comput.Re(data,2)
       list_00.append(z0[0])
       list_01.append(z0[2])
       list_02.append(z0[3])
       list_10.append(z1[0])
       list_11.append(z1[2])
       list_12.append(z1[3])
       list_20.append(z2[0])
       list_21.append(z2[2])
       list_22.append(z2[3])
D={'code':list_code,'nn_R':list_00,'nn_total':list_01,'nn_score':list_02,
   'svm_R':list_10,'svm_total':list_11,'svm_score':list_12,
   'lr_R':list_20,'lr_total':list_21,'lr_score':list_22}
D=pd.DataFrame(D)
D.to_excel('D.xlsx')