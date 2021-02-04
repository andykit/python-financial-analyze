# -*- coding: utf-8 -*-
import numpy as np
data=np.load('data.npy')
data=data[:,1:]
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(data)
data=imp.transform(data)

from sklearn.preprocessing import StandardScaler
X=data
scaler = StandardScaler()
scaler.fit(X) 
X=scaler.transform(X)

from sklearn.preprocessing import MinMaxScaler   
X1=data
min_max_scaler = MinMaxScaler()
min_max_scaler.fit(X1)
X1=min_max_scaler.transform(X1)



