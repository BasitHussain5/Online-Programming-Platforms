#!/usr/bin/env python
# coding: utf-8

# In[2]:


inp = int(input())
lesser_n = inp%60
lesser_nplus = (inp+1)%60

def fibo(inp):
    x, y = 0, 1
    for _ in range(2, inp+1):
        c = x+y
        c = c% 10
        y, x = c, y
    return c

if lesser_n<=1:
    x = lesser_n
else:
    x = fibo(lesser_n)
if lesser_nplus<=1:
    y = lesser_nplus
else:
    y = fibo(lesser_nplus)

 
print((x*y)%10)


# In[ ]:




