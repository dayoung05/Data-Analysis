#!/usr/bin/env python
# coding: utf-8

# # Chapter 2 파이썬 기본 문법 익히기
# 
# 

# ## 2.1 변수
# 
# * 변수의 개념:  변수는 바구니
# * 변수 선언: 바구니에 값을 넣음
# * 변수 이름: 바구니에 이름을 붙임

# ### 2.1.1 변수란?
# * 변수이름=데이터

# In[25]:


a=5  # a 라는 바구니에 값 5를 넣는다.
a    # a 값을 확인


# In[26]:


b=3  # b 라는 바구니에 값 3을 넣는다. 
b    # b 값을 확인


# In[28]:


a+b


# In[30]:


# 변수에 문자도 넣을 수 있다. 
C='가나다'
C


# In[31]:


# 소수점도 가능
radio_freq = 107.9
radio_freq


# ### 2.1.2 변수 이름 규칙(1)
# * 숫자 시작 변수
# * 공백 포함 변수
# * 기호 포함 변수(밑줄 제외)
# * 예약어

# ### 2.1.3 변수 이름 규칙(2)
# * 대소문자 구분
# * 한 번에 여러 변수 선언 가능
# * 하나의 값을 여러 변수에 담을 수 있다.

# In[32]:


# 대소문자 구분
abc = 5
abc


# In[33]:


# 한 번에 여러 변수 선언 가능
ABC = "Apple"
ABC


# In[34]:


x, y, z = "Apple","Banana", "Carrot"
x


# In[35]:


y


# In[36]:


z


# In[38]:


# 하나의 값에 여러 변수 담을 수 있다.
x = y = z = "Dag"
x


# In[39]:


y


# In[40]:


z


# In[ ]:




