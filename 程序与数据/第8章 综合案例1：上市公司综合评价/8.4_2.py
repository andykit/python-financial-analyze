# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pandas as pd
import ffun
import fun2
data=pd.read_excel('data1.xlsx')
r1=ffun.Fr2(data,2014)
Fscore1=r1[0]
Fscore2=r1[1]
r2=fun2.Re(Fscore1,'2015-05-01','2015-12-31',20)
r_list=r2[0]
r_total=r2[1]

