
import pandas as pd
x=pd.read_excel('TRD_Cale.xlsx')
list1=['2017-01-03']
list2=[]
for t in range(1,len(x)-1):
    p=x.iloc[t-1,[2]][0]
    q=x.iloc[t,[2]][0]
    if q<p:
        list1.append(x.iloc[t,[1]][0])
        list2.append(x.iloc[t-1,[1]][0])
list2.append('2017-12-29')

data=pd.read_excel('IDX_Idxtrd.xlsx')

import numpy as np
r=np.zeros(len(list1))
for i in range(len(list1)):
    p1=data.loc[data['Idxtrd01'].values==list1[i],'Idxtrd05'].values
    p2=data.loc[data['Idxtrd01'].values==list2[i],'Idxtrd05'].values
    r[i]=(p2-p1)/p1
  
