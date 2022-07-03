#!/usr/bin/env python
# coding: utf-8

# In[5]:


abc=5
def average(prices, abc):
    total = 0 
    print('num is : ',num)
    print('abc inside function is : ',abc)
    for price in prices: 
        total = total + price 
    avg = total/len(prices)
    return avg
numbers = [1,2,3,4,5]
num = 10 
my_average = average(numbers, num)
print('abc outside function is : ',abc)
print(my_average) 
#print(price)
print(len(numbers))


# In[7]:


order_goal = 25
def average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    avg = total/len(numbers)
    return avg


# In[9]:


def main():
    prices = [29, 21, 55, 10]
    result = average(prices)
    print(order_goal)
    print(result)
main()
#print(len(prices))
print(len(numbers))


# In[39]:


name="ashim das"             # string.count('c')=counts total no of charectors that occur
name.count("ashim")


# In[68]:


name=('ashim')
name.count("name") #str.count(" counts total no of occurance of any charectors")


# In[20]:


name="ashim"
str.capitalize(name)


# In[27]:


str='ashim'     """" string.endswith("him"):-tell whether the string ends
                           with "him" or not"""
str.endswith("him")


# In[69]:


str='ashim'   """" string.find("him"):-tell whether the string have this word
                        int it (eg:- "him") or not ."""
str.find("i")


# In[37]:


name='ashim'      """" string.replace(oldword,newword):-the old word is 
                       replaced by new word."""
title='sanu'
str.replace(name,title)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




