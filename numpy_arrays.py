#!/usr/bin/env python
# coding: utf-8

# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with the element type float.

# In[1]:


import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return(numpy.array(arr[::-1], float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

