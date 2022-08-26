#!/usr/bin/env python
# coding: utf-8

# In[26]:


def print_name(name):
    print("Hello World")


# In[27]:


print_name("Ashim")


# In[40]:


def my_func(name):
    print(" hi!!")


# In[41]:


my_func("Chall Hatt")


# In[44]:


def print_age(name, age):
    print(f"Hi {name} , How are you ??")
    print(f"{name} today you turning  to {age} years old")
        


# In[43]:


print_age("Ashim", 20)


# In[45]:


def cal_age(birth_year):
     return 2022 - birth_year


# In[46]:


cal_age(2002)


# ###  Some Important Things 

# In[47]:


ord('A') # ord :-( Order ) same as ascii code 


# In[48]:


for c in range(65, 65+26):
    print(f"{c} is {chr(c)}")


# In[49]:


hours  = 50
hours % 24


# In[60]:


def is_even(n):
    if n % 2 ==0 :
         print("Even")
    else :
         print("Odd")
    


# In[61]:


is_even(4)


# In[82]:


def encrpt_char(char, key):
    return  chr(ord('A') + (ord(char) - ord('A') +  key) % 26)


# In[83]:


def encrpt_message(message, key):
    message =  message.upper()
    cipher = ''
    for c in message:
        if c in ' ., ':
            cipher =  cipher + c
        else:
            cipher = cipher + encrpt_char(c, key)
    return cipher


# In[84]:


encrpt_message("you are awesome", 3)


# In[85]:


def decrpt_char(char, key):
     return  chr(ord('A') + (ord(char) - ord('A') + 26 -  key) % 26)


# In[88]:


def decrpt_message(cipher, key):
    message = ''
    
    for c in cipher:
        if c in ' ., ':
            message =  message + c
        else:
            message = message + decrpt_char(c, key)
    return message


# In[89]:


decrpt_message('BRX DUH DZHVRPH', 3)


# In[90]:


def decrpt_message2(cipher, key):
    return encrpt_message(cipher, 26- key)


# In[91]:


decrpt_message('BRX DUH DZHVRPH', 3)


# In[86]:


decrpt_char('D', 3)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




