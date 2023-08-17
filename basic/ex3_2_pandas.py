#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
data = {'학번': range(2000, 2010), '성적': [85, 95, 75, 70, 100, 100, 95, 85, 80, 85]}
df = pd.DataFrame(data, columns = ['성적', '학번'])
df


# In[11]:


index = range(ord('a'), ord('j'))
index


# In[12]:


data = {'학번': range(2000, 2010), '성적': [85, 95, 75, 70, 100, 100, 95, 85, 80, 85]}
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, columns = ['성적', '학번'], index = index)
df


# In[22]:


dd = pd.read_csv('CARD_SUBWAY_MONTH_202307.csv', index_col = False)
dd


# In[25]:


dd.head()


# In[26]:


dd.shape


# In[27]:


dd.tail()


# In[28]:


df.describe()


# In[30]:


df.info()


# In[31]:


df['노선명'].unique()


# In[32]:


df['노선명'].value_counts()


# In[33]:


df.sort_values(by=['승차총승객수'])


# In[34]:


df.sort_values(by=['승차총승객수'], ascending=False)


# In[35]:


df['노선명']


# In[36]:


df[0:10]


# In[37]:


df.iloc[1]


# In[40]:


df2 = df.set_index('사용일자')
df2.head(3)


# In[41]:


df2.iloc[1]


# In[53]:


df2.loc[20230702]


# In[46]:


df['노선명'] == '2호선'


# In[47]:


df[df['노선명'] == '2호선']


# In[48]:


df[df['승차총승객수'] >= 50000]['역명'].unique()


# In[49]:


df2['승차총승객수'].max()


# In[50]:


df2['승차총승객수'].idxmax()


# In[51]:


df2['승차총승객수'].argmax()


# In[54]:


df2.iloc[11739]


# In[55]:


df.drop(0)


# In[56]:


df.drop(['등록일자'], axis=1)


# In[57]:


df['승차총승객수']+2


# In[60]:


df['승하차총승객수차이'] = df['승차총승객수'] - df['하차총승객수'] 
df.head()


# In[62]:


df['승하차총승객수차이'].mean()


# In[64]:


sample_df = df.sample(n=10)
sample_df


# In[65]:


sample_df['노선명'].replace(['1호선', '2호선', '3호선', '4호선'], ['line1', 'line2','line3','line4'])


# In[68]:


def getData(data):
    data = str(data)
    year = data[0:4]
    month = data[4:6]
    day = data[6:8]
    return '{}-{}-{}'.format(year, month, day)
getData(12345667)


# In[69]:


df['사용일자'].apply(getData)


# In[72]:


df['사용일자1'] = df['사용일자'].apply(getData)
df['사용일자1'].astype('datetime64')


# In[73]:


df['승차총승객수'].apply(lambda x: x+2)


# In[75]:


plus2 = lambda x: x+2
df['승차총승객수'].apply(plus2)


# In[77]:


dummies = pd.get_dummies(sample_df['노선명'], prefix='노선')
dummies


# In[11]:


import numpy as np
import pandas as pd
na_data = {
    '학번': range(2000, 2010),
    '국어성적': [85, 95, 75, 70, 100, np.nan, 95, 85, 80, 85],
    '영어성적': [95, 70, 100, 85, 80, 85, 95, 95, np.nan, 70],
    '수학성적': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 95, np.nan, 70]
}
na_df = pd.DataFrame(na_data)
na_df


# In[12]:


na_df.isna()


# In[13]:


na_df.isna().sum()


# In[14]:


na_df.fillna(0)


# In[16]:


na_df['수학성적'].fillna(50, inplace=True)
na_df


# In[17]:


na_df.dropna()


# In[23]:


na_df


# In[35]:


df = pd.read_csv('CARD_SUBWAY_MONTH_202307.csv', index_col = False)
df.groupby(['노선명']).mean(numeric_only=True)


# In[26]:


df


# In[42]:


df1 = pd.DataFrame({
    '이름': ['A', 'B', 'D'],
    '성별': ['남자', '여자', '남자']
})
df2 = pd.DataFrame({
    '이름': ['A', 'B', 'C'],
    '키': [180, 160, 150]
})
pd.merge(df1, df2)


# In[45]:


df3 = pd.merge(df1, df2, how='outer')
df3


# In[60]:


df3.to_csv('dataframe2.csv', encoding='euc-kr')


# In[48]:


df3.to_csv('dataframe3.csv', encoding='euc-kr', index=False)


# In[53]:


df3.to_csv('dataframe4.csv', encoding='euc-kr', header=False)


# In[61]:


df4 = pd.read_csv('dataframe2.csv', encoding='euc-kr', index_col = 0)


# In[62]:


df4


# In[ ]:




