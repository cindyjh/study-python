#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
list1 = [1, 2, 3]
arr1 = np.array(list1)
arr1


# In[4]:


np.zeros(3)


# In[6]:


# 2차원
np.zeros((2, 3))


# In[7]:


# np.arange([시작번호], 끝번호, [건너뛰는 수])
# 끝번호가 필수값이다 ;; 인자 순서 왜저럼 ?
np.arange(10)


# In[8]:


np.arange(20, 30, 2)


# In[11]:


np.random.rand(2, 3)


# In[14]:


arr2 = np.arange(16)
arr2


# In[16]:


arr2.reshape(4, 4)


# In[17]:


arr2.reshape(2,2, 4)


# In[18]:


arr = np.arange(16)
arr


# In[19]:


arr.shape


# In[20]:


arr.dtype


# In[21]:


arr.astype(float)


# In[22]:


arr=np.arange(16)


# In[23]:


arr[5]


# In[24]:


arr[-1]


# In[25]:


arr[5:8]


# In[30]:


arr = np.arange(16).reshape((4,4))
arr


# In[31]:


arr[1]


# In[32]:


arr[1, 2]


# In[33]:


arr[0:2, 2:4]


# In[34]:


arr[:2, 2:]

