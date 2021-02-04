# -*- coding: utf-8 -*-
import pandas as pd
import fun
import fun2
data=pd.read_excel('data.xlsx')
ind300=pd.read_excel('index300.xlsx')
list1=[]
list2=[]
list3=[]
list4=[]
for year in [2013,2014,2015,2016]:
    for time in ['06-30','09-30','12-31']:
        r1=fun.Fr(data,year)
        r2=fun2.Re(r1[0],str(year+1)+'-05-01',str(year+1)+'-'+time,20)
        r_total=r2[1]
        list1.append(year)
        list2.append(str(year+1)+'-05-01'+'--'+str(year+1)+'-'+time)
        list3.append(r_total)
        td1=str(year+1)+'-05-01'
        td2=str(year+1)+'-'+time
        I1=ind300.iloc[:,1].values>=td1
        I2=ind300.iloc[:,1].values<=td2
        dt=ind300.iloc[I1&I2,[1,2]].sort_values('Idxtrd01')
        p=dt.iloc[:,1].values
        list4.append((p[len(p)-1]-p[0])/p[0]) 
D={'year':list1,'time':list2,'r_total':list3,'index':list4}
D=pd.DataFrame(D)
D.to_excel('D.xlsx')


