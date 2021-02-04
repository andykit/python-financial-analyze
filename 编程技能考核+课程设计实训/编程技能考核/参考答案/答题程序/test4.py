tiem=['西红柿','排骨','鸡蛋','毛巾','水果刀','茄子','香蕉','袜子','肥皂','酸奶','土豆','鞋子']
import pandas as pd
import numpy as np
data = pd.read_table('第四题.txt',sep='、',header=None) 
D=dict()
for t in range(len(tiem)):
    z=np.zeros((len(data)))
    li=list()
    for k in range(len(data.iloc[0,:])):
        s=data.iloc[:,k]==tiem[t]
        li.extend(list(s[s.values==True].index))
    z[li]=1
    D.setdefault(tiem[t],z)
Data=pd.DataFrame(D) 
import apriori                 #导入自行编写的apriori函数
outputfile = 'apriori_rules.xls'     #结果文件
support = 0.2                  #最小支持度
confidence = 0.4               #最小置信度
ms = '---'                      #连接符，默认'--'，
apriori.find_rule(Data, support, confidence, ms).to_excel(outputfile)    


