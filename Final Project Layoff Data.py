#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np

import statsmodels.formula.api as sm
import scipy.stats as stats

from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns


# In[4]:


df = pd.read_csv('layoffs_data.csv')
df.head()


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# In[8]:


df.drop(columns = "Funds_Raised", inplace = False)


# In[9]:


df.drop(columns = "Source", inplace = False)


# In[10]:


df.dropna(inplace = False)
df.head()


# In[12]:


dfz = df.copy()
print(dfz.shape)


# In[13]:


dfz["zscore_Laid_Off_Count"] = np.abs(stats.zscore(dfz["Laid_Off_Count"]))
dfz.head()


# In[16]:


z_outliers = dfz.loc[dfz["zscore_Laid_Off_Count"] > 3].index
print(z_outliers)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




