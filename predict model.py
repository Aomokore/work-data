#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# In[38]:


tickers=['AAPL', 'MSFT', 'SPY', 'GS']
header = ['Open', 'High', 'Low', 'Close', 'Adj Close']
df = yf.download(tickers, start="2017-01-01", end="2023-04-01")
df= df.dropna()


# In[39]:


df.to_csv('data.csv')


# In[45]:


df= pd.read_csv('data.csv')
df.head(10)


# In[46]:


df.info()


# In[47]:


df.shape


# In[48]:


df.describe


# In[53]:


df.corr()


# In[54]:


from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


# In[56]:


X= df.iloc[:,1:14]   
Y= df.iloc[:,-1]  


# In[57]:


best_features= SelectKBest(score_func=chi2, k=3)
fit= best_features.fit(X,Y)


# In[ ]:




