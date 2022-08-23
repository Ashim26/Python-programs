#!/usr/bin/env python
# coding: utf-8

# ### Lists 
# 
# Sequence of data

# In[2]:


my_list = ['Apple','Banana','Orange']


# In[3]:


my_list


# In[5]:


my_list[1]


# In[6]:


my_list[-1]


# In[7]:


my_list.pop() # .pop :- Remove and Return item at index (default last)


# In[8]:


my_list


# In[9]:


my_list.append("Orange") # adds an element to the list


# In[11]:


my_list


# In[29]:


your_list =  ['New_Delhi','Bhubaneswar','Odisha']


# In[13]:


new_list = my_list+your_list #Concatinating the two list 


# In[14]:


new_list


# Using Random  Here

# In[16]:


import random


# In[27]:


random.choice(new_list)


# In[33]:


random.shuffle(new_list) #random.shuffle :- Shuffle list x in place and return None 


# In[34]:


new_list


# In[35]:


' '.join(new_list)  #  ' '.join(new_list)command joins the element present with a space 
                   


# In[36]:


''.join(new_list)   # ''.join(new_list)command joins the element present without a space 


# In[ ]:





# In[46]:


s = "awesome"
random.sample(s,len(s)) # sample word is 'awesome' 
                        # random.sample command picks randomly the variables and 
              # shows the o/p


# In[44]:


s = "awesome"
''.join(random.sample(s,len(s)))


# In[ ]:


# Declaring another list 
my_number =  [3,4,5,6,9,8,7,20]


# In[ ]:


my_number


# In[ ]:


max(my_number)

min(my_number)
# In[52]:


sum(my_number)


# In[53]:


len(my_number)


# In[57]:


avg = sum(my_number)/len(my_number)
avg


# ### Project 
# #### Word Puzzle
# A word jumbel is a word puzzle game that presents the player wieth a buch of mixed up letters and require shem to unscramble it and to find the hidden word
# 
# Points:-
# 1. The computer will take the word and unsramble it (mix up the letters)
# 2. Then the letter will guess what the word is 
# 
# Initial word that can be used up to keep it in the list [ 'father', 'enterprice', 'Science',  'programming', 'resistance', 'fiction', 'condition','reverse', ' computer','python']

# In[3]:


import random


# In[1]:


words = [ 'father', 'enterprice', 'science',  'programming', 'resistance', 'fiction', 'condition','reverse', ' computer','python']


# In[4]:


jumbled_word = random.choice(words)  # We are storing random choice to jumbled words 

jumbled_word


# In[5]:


random.sample(jumbled_word, len(jumbled_word))


# In[6]:


print("Enter the word Correct word To Win the Puzzle Game ....")
word = input("Initial Word is...  ")
if word == jumbled_word:
    print("Correct Answer !!")
elif word != jumbled_word:
    print("Wrong Answer ",jumbled_word,"Is correct answer" )  #for correct answer


# In[7]:


print("Enter the word Correct word To Win the Puzzle Game ....")
word = input("Initial Word is...  ")
if word == jumbled_word:
    print("Correct Answer !!")
elif word != jumbled_word:
    print("Wrong Answer ",jumbled_word,"Is correct answer" ) # for wrong answer


# In[ ]:




