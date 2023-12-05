#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import re


# In[98]:


df = pd.read_csv(r'C:\\Users\\Neil Garcia\\adventofcode\\day1\\data.txt', header=None)


# In[99]:


df


# In[101]:


def extract (word):
    word = re.findall('\d+', word)
    word = "".join(word)
    return word


# In[102]:


df[1] = df[0].apply(extract)


# In[103]:


df


# In[128]:


def getnumber (number):
    firstNum = number[0]
    lastNum = number[-1]
    number = firstNum,lastNum
    number = "".join(number)
    return int(number)


# In[129]:


df[2] = df[1].apply(getnumber)


# In[130]:


df


# In[131]:


Total = df[2].sum()
print(Total)

