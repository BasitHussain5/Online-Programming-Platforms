#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x, y = [int(i) for i in input().split()]
    
def computeGCD(x, y): 
    while(y):
        x, y = y, x % y 
        
    return x 
  
print (computeGCD(x,y)) 


# In[ ]:




