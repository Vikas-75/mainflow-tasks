#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# In[3]:


data = pd.read_csv('C:\\Users\\VIKAS MALI\\Downloads\\householdtask3.csv')


# In[4]:


display(data.head(10))


# In[ ]:





# In[5]:


#scatter plot with year against own
plt.scatter(data['year'], data['own'])

#Adding title to the plot
plt.title("Scatter plot")

#setting the x and y label
plt.xlabel('year')
plt.ylabel('own')

#Setting the result
plt.show()



# In[6]:


#line CHart with year against own
plt.plot(data['year'])
plt.plot(data['own'])

#Adding title to the plot
plt.title("line chart")

#setting the x and y label
plt.xlabel('year')
plt.ylabel('own')

#Setting the result
plt.show()


# In[7]:


#Bar chart or bar plot
plt.bar(data['year'],data['own'])

#Adding title to the plot
plt.title("Bar chart")

#setting the x and y label
plt.xlabel('year')
plt.ylabel('own')

#Setting the result
plt.show()



# In[8]:


#Histogram
plt.hist(data['income'])

plt.title("Histogram")

plt.show()


# In[ ]:




