#!/usr/bin/env python
# coding: utf-8

# # Tuples
# 
# ### Can contain any number of items
# ### Can contain different types of items
# ### Cannot be altered once created (they are immutable)
# ### Items have a defined order
# 
# #### A tuple is created by using round brackets around the items it contains, with commas seperating the individual elements
# 

# In[1]:


a = (123, 54, 92) # tuple of 4 integers
b = () # empty tuple
c = ("Ala",) # tuple of a single string (note the trailing ",")
d = (2, 3, False, "Arg", None) # a tuple of mixed types

print(a)
print(b)
print(c)
print(d)


# ### Lists
# #### Can cointain any numbers of items
# #### It is mutable
# 
# # Lists are created in with square brackets 

# In[2]:


a = [1, 3, 9, 'Py', 217.213] # List can cointain different data types
b = ["Python"]
c = []

print(a)
print(b)
print(c)


# Lists and tuples can contain other list and tuples,

# In[3]:


matrix = [[input(),input()], [input(),input()]]
print(matrix)

# input() = tuple
# ["Lists"] within square brackets it can store lists also


# ### we can explicitly convert lists into tuples and vice-versa

# In[4]:


a = (1, 4, 9, 16)     # A tuple of numbers
b = ['A','B','C','d'] # A list of characters

print(a)
print(b)

l = list(a)   # Make a list based on a tuple 
print(l)

t = tuple(b)  # Make a tuple based on a list
print(t)


# #### Elements can access individualy by using their index , note that the first element is at index 0. 
# ### Negative indices count backwards from the end.

# In[5]:


t = (123, 54, 92, 87, 33)
x = [123, 54, 92, 87, 33]

print('t is', t)
print('t[0] is', t[0])
print('t[2] is', t[2])

print('x is', x)
print('x[-1] is', x[-1])


# ### Slices
# #### range of items can be accessed from lists and tuple using " : " to mark the begging and ending of slice.

# In[6]:


t = (123, 54, 92, 87, 33)
x = [123, 54, 92, 87, 33]
print('t[1:3] is', t[1:3])
print('x[2:] is', x[2:])
print('x[:-1] is', x[:-1])


# In[7]:


# in Operator :- checks if the value wherther it's is present or not

t = (123, 54, 92, 87, 33)
x = [123, 54, 92, 87, 33]
print('123 in', x, 123 in x)
print('234 in', t, 234 in t)
print('999 not in', x, 999 not in x)


# In[8]:


# len() :- can get length of a list or tuple with the in-built len() function
#count() :-can count the number of particular elements contained in a list with the .count() function.

t = (123, 54, 92, 87, 33)
x = [123, 54, 92, 87, 33]
print("length of t is", len(t))
print("number of 33s in x is", x.count(33))


# In[9]:


### list can be altered
x = [123, 54, 92, 87, 33]
print(x)
x[2] = 33
print(x)


# In[10]:


# tuples are immutable
t = (123, 54, 92, 87, 33)
print(t)
t[1] = 4


# In[11]:


# By append funtion  we can add elements to the list.
x = [123, 54, 92, 87, 33]
x.append(101)
print(x)


# In[12]:


# insert values at a certain position with insert(),
# by supplying the desired position as well as the new value.
x = [123, 54, 92, 87, 33]
x.insert(3, 1111)
print(x)


# In[13]:


#You can remove values with remove()
x = [123, 54, 92, 87, 33]
x.remove(123)
print(x)


# In[14]:


# delete values by index with del
x = [123, 54, 92, 87, 33]
print(x)
del x[0]
print(x)


# ####  It's often useful to be able to combine arrays together, which can be done with extend() (as append would add the whole list as a single element in the list).
# 
# ### can use + operator.

# In[15]:


a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)
a.append(b)
print(a)


# In[16]:


#You can change the order of elements in a list
a = [1, 3, 5, 4, 2]
a.reverse()
print(a)
#print(a[::2])
a.sort()
print(a)


# ### String
# Strings are a lot like tuples of characters.
# 

# In[17]:


text = "ABCDEFGH"
print(text[0])
print(text[-2])
print(text[0:6])
print("EFG" in text)
print("ABC" in text)
print(len(text))


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





# In[ ]:





# In[ ]:




