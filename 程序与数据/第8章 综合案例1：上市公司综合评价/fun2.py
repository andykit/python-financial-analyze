# -*- coding: utf-8 -*-
def Re(Fscore1,s_trd1,s_trd2,num):
   #输入：
   #Fscore1--排名结果（股票代码形式）
   #s_trd1--持有期开始日期
   #s_trd1--持有期结束日期
   #num--排名数
   #输出：
   #r_list--股票代码收益率列表
   #r_total--总收益率
   import pandas as pd
   trd=pd.read_excel('trd_'+s_trd1[0:4]+'.xlsx')
   r_list=[]
   for i in range(num):
       code=Fscore1.index[i]
       dt=trd.iloc[trd.iloc[:,0].values==code,:]
       I1=dt['Trddt'].values>=s_trd1
       I2=dt['Trddt'].values<=s_trd2
       dtt=dt.iloc[I1&I2,:].sort_values('Trddt')
       if len(dtt)>1:
          p1=dtt.iloc[0,3]
          p2=dtt.iloc[len(dtt)-1,3]
          r_list.append((p2-p1)/p1)
   
   r_total=sum(r_list)
   return (r_list,r_total)
   

