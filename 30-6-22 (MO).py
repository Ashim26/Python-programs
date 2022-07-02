#!/usr/bin/env python
# coding: utf-8

# In[6]:


A='10'
B=A+'1'
print(A)
print(B)


# #rounding a even no results in the number itself(0<.5)
# #rounding a odd no results in the one number more than itself(0>.5)

# In[7]:


x= 20
print(id(x))


# In[8]:


x= 20
print(id(x))


# In[9]:


y= 20
print(id(x))


# In[10]:


z= 20
print(id(x))


# ## why in the above case the id of 3 objects are same even if the variables are different ?

# In[12]:


x = str(3.5)
print(type(x))
print(id(x))


# In[17]:


"hello"<="helasn"


# ## slang = {}
# ## slang['cheerio'] = 'goodbye'
# 
# ### here [' cheerio '] is a key that is associated slang and to slang['cheerio'] goodbye is assigned .
# 
# OR slang['cheerio'] stores the goodbye
# 
# 

# In[18]:


slang = {}
slang[1] = 'goodbye'
slang[('smashing',6,':')] = 'terrific' 
slang['knackered']  = ['tired',1, 5]
slang[('knackered',1 ,( 1, 3))] = ['tired',1, 5,[1,(1,2),'Hello']]
print(slang)


# ### above here the last line will be executed.
# which cointains the the key value as the [('knackered',1 ,( 1, 3))]= 
# and slang[('knackered',1 ,( 1, 3))] stores the values  this =
#                                     ['tired',1, 5,[1,(1,2),'Hello']]

# In[20]:


slang[1] = 'goodbye'
print(slang[1])


# In[22]:


slang[('smashing',6,':')] = 'terrific' 
print(slang[('smashing',6,':')])


# In[28]:


slang[('knackered',1 ,( 1, 3))] = ['tired',1, 5]
print(slang[('knackered')])


# In[29]:


slang[('knackered',1 ,( 1, 3))] = ['tired',1, 5,[1,(1,2),'Hello']]
print(slang[('knackered',1 ,( 1, 3))])


# In[ ]:





# In[3]:


import random 
r1= random.random() 
print(r1)


# In[ ]:





# In[ ]:




