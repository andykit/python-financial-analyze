# -*- coding: utf-8 -*-
import pandas as pd
data = pd.read_excel('credit.xlsx')
x = data.iloc[:600,:14].as_matrix()
y = data.iloc[:600,14].as_matrix()
x1= data.iloc[600:,:14].as_matrix()
y1= data.iloc[600:,14].as_matrix()
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5,2), random_state=1)
clf.fit(x, y);
rv=clf.score(x,y)
R=clf.predict(x1)
Z=R-y1
Rs=len(Z[Z==0])/len(Z)
print('预测结果为：',R)
print('预测准确率为：',Rs)


