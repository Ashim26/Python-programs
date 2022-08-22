#!/usr/bin/env python
# coding: utf-8

# ### Random 
# 

# In[13]:


import random
# a = random.randint(1, 10)
# print(a)


# In[26]:


a = random.randint(1, 10) 
print(a)            # random function has to be imported before using it


# In[29]:


random.randint(1, 6)


# In[49]:


random.uniform(0, 1)


# #### Q1.Math Game
# 1.Get a random integer from the range 1 to 10 (both inclusive)
# 2.Get another random integer from the range 1 to 10 (both inclusive)
# 3.Promt the user for what the two integers multiplied 
# 4.Print if correct or not , if not correct , print the correct answer 

# In[60]:


import random

a = random.randint(1, 10)
print(a)
b = random.randint(1, 10)
print(b)
ans= input(f"what is  {a} times  {b}? ")
ans =  int(ans)
if ans == a*b:
   print("correct answer",a*b)
else :
   print("Not Correct .")


# ### Stone - Paper - Scissor Game

# In[73]:


print("Enter your choice 1.Rock 2. paper 3. Scissor")
choice = input("Choice (1/2/3)")
choice = int(choice)
print(f"your choice is {choice} ")

computer_choice = random.randint(1, 3)
print(f"Computer's choice is {computer_choice}")

if choice == computer_choice:
    print("Draw !!")
    print("Shuffle again")
elif choice == 1:
    if computer_choice ==2:
      print("Paper wins Computer wins")
    
    if computer_choice ==3:
      print("Rock wins You win")

elif choice == 2: #Paper
    if computer_choice ==1:#Rock
      print("Paper wins You win")
    
    if computer_choice ==3:#Scissor
      print("Scissor wins Computer wins")
    
elif choice == 3:#Scissor
    if computer_choice ==1:#Rock
      print("Rock  wins Computer wins")
    
    if computer_choice ==2:
      print("Scissor wins You win")
    
       


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




