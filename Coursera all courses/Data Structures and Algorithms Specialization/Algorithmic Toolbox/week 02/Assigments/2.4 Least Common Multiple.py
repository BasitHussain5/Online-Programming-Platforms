#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x, y = [int(i) for i in input().split()]

def euclid_gcd(x, y):
    if y == 0:
        return x
    c = x%y
    return euclid_gcd(y, c)

if x>y:
    gcd = euclid_gcd(x, y)
else:
    gcd = euclid_gcd(y, x)

print(x*y//gcd)


# In[ ]:




