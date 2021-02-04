# -*- coding: utf-8 -*-
import pandas as pd
data = pd.read_excel('car.xlsx')
x = data.iloc[:1690,:6].as_matrix()
y = data.iloc[:1690,6].as_matrix()
x1= data.iloc[1691:,:6].as_matrix()
y1= data.iloc[1691:,6].as_matrix()
from sklearn import svm
clf = svm.SVC(kernel='rbf')  
clf.fit(x, y) 
rv=clf.score(x, y);
R=clf.predict(x1)
Z=R-y1
Rs=len(Z[Z==0])/len(Z)
print('预测结果为：',R)
print('预测准确率为：',Rs)

