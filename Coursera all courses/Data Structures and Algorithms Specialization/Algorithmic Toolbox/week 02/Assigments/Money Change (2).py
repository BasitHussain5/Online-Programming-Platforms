#!/usr/bin/env python
# coding: utf-8

# In[1]:


def change(money):
    numCoins = 0
    while money > 0:
        if money >= 10:
            money -= 10
        elif money >= 5:
            money -= 5
        else:
            money -= 1
        numCoins += 1
    return numCoins
print(change(int(input())))


# In[ ]:




