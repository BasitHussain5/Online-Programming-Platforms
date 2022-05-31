#!/usr/bin/env python
# coding: utf-8

# In[3]:


inp = int(input())

if inp<=1:
    print(inp)  
    quit()


less = (inp+2)%60
if less==1:
    print(0)
    quit()
elif less==0:
    print(9)
    quit()
def fibo(inp):
    a,b = 0, 1
    for _ in range(2,less+1):
        z = a+b
        z = z%10
        b, a = z, b
    if z!=0:
        print(z-1)
    else:
        print(9)
fibo(less)


# In[ ]:




