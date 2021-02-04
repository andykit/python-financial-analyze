import pandas as pd
import numpy as np
x=pd.read_excel('交易日历数据表.xlsx')
x=x.iloc[1700:,:]
list1=[]
list2=[]
for m in np.arange(1,13):
    if m<10:
        d1=str(2017)+'-0'+str(m)+'-01'
        d2=str(2017)+'-0'+str(m)+'-31'
    else:
        d1=str(2017)+'-'+str(m)+'-01'
        d2=str(2017)+'-'+str(m)+'-31'
    I1=x.iloc[:,1]>=d1
    I2=x.iloc[:,1]<=d2
    I=I1&I2
    xs=x.iloc[I.values,[1]]['Clddt'].sort_values()
    if len(xs)>1:
         list1.append(xs.values[0])
         list2.append(xs.values[len(xs)-1])
         
trd=pd.read_excel('IDX_Idxtrd.xlsx')         
Icode=[801200,801770,801790,801020,801110]
list1_=[]
list2_=[]
list3_=[]
list4_=[]
list5_=[]
for t in range(len(Icode)):
    dt=trd.loc[trd['Indexcd'].values==Icode[t],['Idxtrd01','Idxtrd05']]
    for k in range(1,len(list1)):
        p1=dt.loc[dt['Idxtrd01'].values==list1[k],'Idxtrd05'].values
        p2=dt.loc[dt['Idxtrd01'].values==list2[k],'Idxtrd05'].values
        if t==0:
           list1_.append(p2-p1)
        if t==1:
           list2_.append(p2-p1)
        if t==2:
           list3_.append(p2-p1)
        if t==3:
           list4_.append(p2-p1)
        if t==4:
           list5_.append(p2-p1)
UD={'商业贸易':list1_,'通信':list2_,'非银金融':list3_,'采掘':list4_,'家用电器':list5_}
U=pd.DataFrame(UD,index=range(2,len(list1)+1))
           
dta=pd.read_excel('申万行业分类.xlsx')
stkcd=dta.loc[dta['行业名称'].values=='家用电器','股票代码'].values
ddata=pd.read_excel('ddata.xlsx')
s=ddata['Stkcd'].values
I=s==stkcd[0]
for i in range(1,len(stkcd)):
    I1=s==stkcd[i]
    I=I|I1
dt=ddata.iloc[I,:]
import fun
r=fun.Fr(dt,'2016')
c=r[0]
fname=r[1][0:20]
code=list(c.index[0:20])

DA=pd.read_excel('trd_2017.xlsx')
list_r=[]
for i in range(len(code)):
   dat=DA.iloc[DA.iloc[:,0].values==code[i],:]
   dat=dat.sort_values('Trddt')
   r_c=0
   for k in range(1,len(list1)-1):
       I1=dat.iloc[:,1].values>=list1[k+1]
       I2=dat.iloc[:,1].values<=list2[k+1]
       I=I1&I2
       p=dat.iloc[I,3].values
       if len(p)>0:
          r=(p[len(p)-1]-p[0])/p[0]
          if list3_[k-1]>0:
             r_c=r_c+r
   list_r.append(r_c)
s_list=sum(list_r)
m_list=np.mean(list_r)
             
          
       

    


 
    