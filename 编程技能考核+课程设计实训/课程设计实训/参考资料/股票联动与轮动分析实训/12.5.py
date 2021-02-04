# -*- coding: utf-8 -*-
import pandas as pd
td=pd.read_excel('交易日历数据表.xlsx')
I1=td['Clddt'].values>'2017-01-01'
I2=td['Clddt'].values<'2017-12-31'
I=I1&I2
ddt=td.loc[I,['Clddt']]
M=len(ddt)

data=pd.read_excel('DA.xlsx')
code_record=data.iloc[:,0].value_counts()
code=list(code_record[code_record==M].index)

stk=pd.read_excel('TRD_Co.xlsx')
sname=pd.Series(list(stk.iloc[:,1]),index=stk.iloc[:,0])

import numpy as np
D=dict()
for t in range(len(code)):
   dt=data.loc[data['Stkcd']==code[t],['Trddt','Clsprc']].sort_values('Trddt')
   dt1=dt.iloc[0:-1,[1]]['Clsprc'];
   dt2=dt.iloc[1:,[1]]['Clsprc'];
   z21_up=np.zeros(len(dt1))
   z21_up[dt2.values-dt1.values>0]=1
   D.setdefault(sname[code[t]]+'_up',z21_up)
   
Data=pd.DataFrame(D,index=td['Clddt'].values[1:])
import OneRule as OR
r=OR.rule(Data,0.3,0.67)

