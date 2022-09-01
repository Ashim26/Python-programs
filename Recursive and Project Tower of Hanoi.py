#!/usr/bin/env python
# coding: utf-8

# ## Recursion

# In[1]:


def count(n): # defining a function n named as count
    if n <= 0: # for recursion till 0 from a 'n'
        return n #final step where n = 0 
    return n + count(n -1) 


# In[2]:


count(6) # 1.(n= 6:-)  n + count(n -1)  = 6 + count(6-1=5), now new value for n is 5
         # 2.(n= 5:-)  n + count(n -1)  = 5 + count(5-1=4), now new value for n is 4
         # 1.(n=4 :-)  n + count(n -1)  = 4 + count(4-1=3), now new value for n is 3
         # 1.(n= 3:-)  n + count(n -1) = 3+ count(2-1=1), now new value for n is  2
         # 1.(n= 2:-)  n + count(n -1) = 2 + count(2-1=1), now new value for n is 1
         # 1.(n= 1:-)  n + count(n -1)   1 + count(1-1=0), now new value for n is 0
#             when n =0 then this condition  
#             if n <= 0: # for recursion till 0 from a 'n'
#                  return n
#             returns the value of n i.e is 0.


# In[13]:


def count(n): # defining a function n named as count
    if n <= 1: # for recursion till 0 from a 'n'
        return n #final step where n = 0 
    return n * count(n -1) 


# In[14]:


count(5)


# ###   Fibonacci Number
# 

# f0 = 0 
# f1 = 1
# f2 = f0+f1(0+1  = 1)
# f3 = f2 + f1 (1 + 1 = 2)
# .
# .
# f(n) = f(n-1) + f(n-2)

# In[6]:


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


# In[7]:


fib(3)


# ##   Project :- Tower Of Hanoi Project

# ## Recursion 
# 
#    That is the formula . It is all you need to know.
#   1.Move the smaller problem of 2 disks from first tower(rod) to second              tower(rod)
#   2.Move the Big disk from the first tower(rod) to last tower (rod).
#   3.Move the smaller problem of2 disks from second tower(rod) to last   
#      tower(rod).

# ## Steps :-
#  1. Represent the towers as [ [3,2,1],[],[] ].
#  2.Create a move function , wich takes the towers and can move a disk from one tower to another (# Hint Use .pop() and .append(.))
#  3. Make a helper function to print the towers 
#    (Hint Assume that awe have 3  towers and 3 disks )
#   
#   4.The recursive function
#      .Solve_tower_of_hanoi(towers, n , start_tower, dest_tower, aux_tower)
#   5. n is the no of disks we move, starting with 3 , then we call recrusive       down with 2,1,0.
#   6.The base case is n =0 , just return in that case
#   . Move subproblem of n-1 disks from start_tower to aux_tower 
#   . Move disk n to dest_tower .(You can print the tower here is you like )
#   . Move subproblem of n-1 disk from aux_tower to dest_tower.

# In[3]:


towers = [[3,2,1],[],[]]
   


# In[4]:


towers


# In[5]:


towers[2]


# In[6]:


def move(towers, from_tower, dest_tower):
    disk = towers[from_tower].pop()
    towers[dest_tower].append(disk)
    return towers


# In[7]:


towers = move(towers, 0, 2)


# In[8]:


towers


# In[9]:



towers = move(towers, 2, 0)


# In[56]:


towers


# In[36]:


def print_towers(towers):
    for i in range(3, 0, -1):
        for tower in towers:
            if len(tower) >= i:
                print(tower[i - 1], end='  ')
            else:
                print('|', end='  ')
        print()
    print('-----')


# In[37]:


print_towers(towers)


# In[38]:


def solve_tower_of_hanoi(towers, n , start_tower, dest_tower, aux_tower):
    if n==0:
        return
    # Move  subproblem of n-1 disks from start_tower to aux_tower
    solve_tower_of_hanoi(towers, n - 1, start_tower, aux_tower, dest_tower)
    
    # Move disk n to dest_tower.(you can print the tower here is you like)
    move(towers, start_tower, dest_tower)
    print_towers(towers)
    
    # Move subproblem of n-1 disk from aux_tower to dest_tower
    solve_tower_of_hanoi(towers, n - 1, aux_tower, dest_tower , start_tower)
    
    
    
     


# In[39]:


towers = [[3 ,2 , 1], [],[]]
print_towers(towers)
solve_tower_of_hanoi(towers, 3, 0, 2, 1)


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





# In[ ]:




