# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
L=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  #列表
T=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)  #元组
A=np.array(L)                      #将列表L转换为数组，赋给变量A
S=pd.Series(L)                      #将列表L转换为序列，赋给变量S
#avg_L=pd.rolling_mean(L,10)   #报错
#avg_T=pd.rolling_mean(T,10)   #报错
avg_S=pd.rolling_mean(S,10)
avg_A=pd.rolling_mean(A,10)

sum_S=pd.rolling_sum(S,10)
sum_A=pd.rolling_sum(A,10)
Min_S=pd.rolling_min(S,10)
Min_A=pd.rolling_min(A,10)
Max_S=pd.rolling_max(S,10)
Max_A=pd.rolling_max(A,10)
