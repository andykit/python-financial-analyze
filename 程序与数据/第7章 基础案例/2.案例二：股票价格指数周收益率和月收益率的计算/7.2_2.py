
import pandas as pd
x=pd.read_excel('TRD_Cale.xlsx')
list1_m=[]
list2_m=[]
import numpy as np
for m in np.arange(1,13):
   if m<10:
     d1='2017-0'+str(m)+'-01'
     d2='2017-0'+str(m)+'-31'
   else:
     d1='2017-'+str(m)+'-01'
     d2='2017-'+str(m)+'-31'
   I1=x.iloc[:,1]>=d1
   I2=x.iloc[:,1]<=d2
   I=I1&I2
   xs=x.iloc[I.values,[1]]['Clddt'].sort_values()
   if len(xs)>1:
      list1_m.append(xs.values[0])
      list2_m.append(xs.values[len(xs)-1])

data=pd.read_excel('IDX_Idxtrd.xlsx')

import numpy as np
r=np.zeros(len(list1_m))
for i in range(len(list1_m)):
    p1=data.loc[data['Idxtrd01'].values==list1_m[i],'Idxtrd05'].values
    p2=data.loc[data['Idxtrd01'].values==list2_m[i],'Idxtrd05'].values
    r[i]=(p2-p1)/p1