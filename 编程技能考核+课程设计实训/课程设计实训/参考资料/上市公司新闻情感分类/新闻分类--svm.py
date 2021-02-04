# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import jieba  #引用结巴分词库
import time   #导入时间模块
import gensim
import pandas as pd
import numpy as np
from gensim import corpora, models, similarities

start = time.clock()  #开始计时
#添加自定义词典

# 创建停用词
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]#停用词List的创建
    return stopwords
 
 
# # 对文档中的每一行进行中文分词
def rm_stop_words(word_list):
    word_list = list(word_list)
    stop_words = stopwordslist('stop_words.txt')
    # 这个很重要，注意每次pop之后总长度是变化的
    for i in range(word_list.__len__())[::-1]:
        # 去停用词
        if word_list[i] in stop_words:
            word_list.pop(i)
        #  去数字
        elif word_list[i].isdigit():
            word_list.pop(i)
    return word_list

rawdata=pd.read_excel('原始数据.xlsx')
dictionary = corpora.Dictionary()

wordcode=[]
y=[]
word_length=[]
textcut_all=[]
for i in range(len(rawdata)):
  text=rawdata.iloc[i,1]
  word_list = list(jieba.cut(text, cut_all=False))
  word_list = rm_stop_words(word_list)
  text_cut=str()
  for k in range(len(word_list)-1):
      text_cut=text_cut+word_list[k]+ ' '
  text_cut=text_cut+word_list[len(word_list)-1]
  textcut_all.append(text_cut)
  
  dictionary.add_documents([word_list])
  word_index=dictionary.doc2idx(word_list)
  wordcode.append(word_index)
  
  word_length.append(len(word_index))
 
  
  if rawdata.iloc[i,0]=='积极':
     y.append(0)
  elif rawdata.iloc[i,0]=='中性':
     y.append(1)
  else:
     y.append(2)   
     

testdata=pd.read_excel('新闻测试数据.xlsx')
testcut_all=[]
for i in range(len(testdata)):
  text=testdata.iloc[i,0]
  word_list = list(jieba.cut(text, cut_all=False))
  word_list = rm_stop_words(word_list)
  text_cut=str()
  for k in range(len(word_list)-1):
      text_cut=text_cut+word_list[k]+ ' '
  text_cut=text_cut+word_list[len(word_list)-1]
  testcut_all.append(text_cut)
  
  dictionary.add_documents([word_list])
  word_index=dictionary.doc2idx(word_list)
  wordcode.append(word_index)
  
  word_length.append(len(word_index))

x=np.array(wordcode)
np.save('x.npy',x[:len(rawdata)])
np.save('x1.npy',x[len(rawdata):])
y=np.array(y)
np.save('y.npy',y)
maxlen=max(word_length)
word_num=len(dictionary)
X=pd.Series(textcut_all)
Y=pd.Series(y)

from sklearn.model_selection import train_test_split 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

count_vect = CountVectorizer() #对CountVectorizer创建对象count_vect
x_train_counts = count_vect.fit_transform(X) #用来对数据进行处理，表示成n-gram的形式
tfidf_transformer = TfidfTransformer()#对TfidfTransformer创建对象tfidf_transformer
X = tfidf_transformer.fit_transform(x_train_counts) 

x_train, x_test, y_train, y_test = train_test_split (X, Y, random_state = 0)



from sklearn.svm import LinearSVC
clf = LinearSVC()
clf.fit(x_train, y_train)
rv2=clf.score(x_train, y_train)
print('支持向量机模型的准确率为：',rv2)

y1=clf.predict(x_test)
r=y1-y_test.values
r=len(r[r==0])/len(r)
print('支持向量机预测的准确率为：',r)

test_y=[]
for i in range(len(testcut_all)):
    text1=testcut_all[i]
    pre=clf.predict(count_vect.transform([text1]))
    test_y.append(pre[0])

end = time.clock()  #
print('运行时间：',end-start)