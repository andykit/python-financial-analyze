# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
data=pd.read_excel('missing.xlsx')                        #数据框data
c=np.array([[1,2,3,4],[4,5,6,np.nan],[5,6,7,8],[9,4,np.nan,8]])   #数组c
C=pd.DataFrame(c)                                    #数据框C

# 1.均值填充策略
from sklearn.preprocessing import Imputer 
fC=C 
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(fC)
fC=imp.transform(fC)

# 2.中位数填充策略
imp = Imputer(missing_values='NaN', strategy='median', axis=1)
fc=c
imp.fit(fc)
fc=imp.transform(fc)

# 3.最频繁值填充策略
fD=data[['a','c']]
imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)
imp.fit(fD)
fD=imp.transform(fD)



