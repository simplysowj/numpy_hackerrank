#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

n,m = map(int,input().split())
a = np.array([input().split() for _ in range(n)],int)
b = np.array([input().split() for _ in range(n)],int)
print(a+b,a-b,a*b,a//b,a%b,a**b,sep="\n")


# In[ ]:




