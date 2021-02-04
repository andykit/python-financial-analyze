# -*- coding: utf-8 -*-
import pandas as pd
path='一、车次上车人数统计表.xlsx';
data=pd.read_excel(path);
data=pd.read_excel(path,'Sheet2')  #读取sheet里面的数据
dta=pd.read_excel('dta.xlsx',header=None)  #无表头

dta1=pd.read_table('txt1.txt',header=None)  #分隔默认为Tab键，设置无表头。
dta2=pd.read_table('txt2.txt',sep='\s+')              #分隔为空格，带表头
dta3=pd.read_table('txt3.txt',sep=',',header=None)  #分隔为逗号，设置无表头