#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data =pd.read_csv('C:\\Users\\VIKAS MALI\\Downloads\\01.Data Cleaning and Preprocessing.csv')


# In[4]:


type(data)


# In[5]:


data.info


# In[6]:


data.describe()


# In[8]:


data = data.drop_duplicates()
data


# In[9]:


data.isnull()


# In[10]:


data.isnull().sum()


# In[12]:


data.notnull()


# In[13]:


data.isnull().sum().sum()


# In[14]:


data2 = data.fillna(value=0)
data2


# In[15]:


data.isnull().sum().sum()


# In[16]:


data2.isnull().sum().sum()


# In[17]:


data


# In[19]:


data3 = data.fillna(method='pad')
data3


# In[20]:


data4=data.fillna(method='bfill')
data4


# In[31]:


import numpy as np
from scipy import stats


# In[34]:


data.columns


# In[35]:


data.drop(['Observation'], axis=1, inplace=True)
data.columns


# In[36]:


Q1= data2.quantile(0.25)
Q3= data2.quantile(0.75)
IQR=Q3-Q1
print(IQR)


# In[37]:


data2=data2[~((data2<(Q1-1.5*IQR))|(data2>(Q3+1.5*IQR))).any(axis=1)]
data2


# In[38]:


data2.describe()


# In[ ]:




