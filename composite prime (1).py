#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math

def primenum(num):
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

prime_list = []
comp_list = []
primesum = 0
compsum = 0
for i in range (2, 1001):
    if primenum(i) == True:
        prime_list.append(i)
    else:
        comp_list.append(i)

print(prime_list)
print("\n")
print(comp_list)
for i in prime_list:
    primesum += i
for i in comp_list:
    compsum += i
finalsum = compsum - primesum
print("Finalsum: " + str(finalsum))


# In[ ]:




