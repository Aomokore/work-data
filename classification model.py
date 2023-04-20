#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Machine learning classification
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
# For data manipulation
import pandas as pd
# To plot
import matplotlib.pyplot as plt
import seaborn
import numpy as np


# In[10]:


# Step 2: Fetch data
import yfinance as yf
Df = yf.download('SPY', start="2017-01-01", end="2023-04-01")
Df = Df.dropna()
Df.Close.plot(figsize=(10,5))
plt.ylabel("S&P500 Price")
plt.show()


# In[11]:


y = np.where(Df['Close'].shift(-1) > Df['Close'],1,-1)


# In[12]:


Df['Open-Close'] = Df.Open - Df.Close
Df['High-Low'] = Df.High - Df.Low
X=Df[['Open-Close','High-Low']]


# In[13]:


split_percentage = 0.8
split = int(split_percentage*len(Df))
# Train data set
X_train = X[:split]
y_train = y[:split]
# Test data set
X_test = X[split:]
y_test = y[split:]


# In[14]:


cls = SVC().fit(X_train, y_train)


# In[15]:


accuracy_train = accuracy_score(y_train, cls.predict(X_train))
accuracy_test = accuracy_score(y_test, cls.predict(X_test))
print('\nTrain Accuracy:{: .2f}%'.format(accuracy_train*100))
print('Test Accuracy:{: .2f}%'.format(accuracy_test*100))


# In[16]:


Df['Predicted_Signal'] = cls.predict(X)
# Calculate log returns
Df['Return'] = np.log(Df.Close.shift(-1) / Df.Close)*100
Df['Strategy_Return'] = Df.Return * Df.Predicted_Signal


# In[17]:


Df.Strategy_Return.iloc[split:].cumsum().plot(figsize=(10,5))
plt.ylabel("Strategy Returns (%)")
plt.show()


# In[ ]:




