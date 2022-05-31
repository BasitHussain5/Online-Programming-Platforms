#!/usr/bin/env python
# coding: utf-8

# In[ ]:


inp = int(input())
if inp<=1:
    print(inp)
def lastdigitfibo(inp):
    x, y = 0, 1
    for _ in range(inp-1):
        c = x + y
        c = c%10
        y, x = c, y
    print(c)

lastdigitfibo(inp)


# In[ ]:




