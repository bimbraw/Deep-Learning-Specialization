#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

a = np.array([1,2,3,4])
print(a)


# In[8]:


import time

a = np.random.rand(10000000)
b = np.random.rand(10000000)

tic = time.time()
c = np.dot(a,b)
toc = time.time()

print(c)
print("Vectorized version:" + str(100000*(toc-tic)) + "us")
vectorized = 1000*(toc-tic)

c = 0
tic = time.time()

for i in range(10000000):
    c += a[i]*b[i]
toc = time.time()

print(c)
print("for loop:" + str(100000*(toc-tic)) + "us")
non_vectorized = 1000*(toc-tic)

print("vectorized is " + str(non_vectorized/vectorized) + " times faster than non-vectorized version")


# In[ ]:




