# -*- coding: utf-8 -*-
S=str()   #产生空字符串

st='hello word!'
z1=st.find('he',0,len(st)) #返回包含子串的开始索引位置，否则-1
z2=st.find('he',1,len(st))
print(z1,z2)

stt=st.replace('or','kl') #原来的st不变
print(stt)
print(st)

st1='joh'
st2=st1+' '+st
print(st2)

str1='jo'
str2='qb'
str3='qb'
s1=str1!=str2
s2=str2==str3
print(s1,s2)


