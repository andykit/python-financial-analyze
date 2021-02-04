# -*- coding: utf-8 -*-
import pandas as pd
import fun
import fun2
data=pd.read_excel('data.xlsx')
r1=fun.Fr(data,2016)
Fscore1=r1[0]
Fscore2=r1[1]
r2=fun2.Re(Fscore1,'2017-05-01','2017-12-31',30)
r_list=r2[0]
r_total=r2[1]
