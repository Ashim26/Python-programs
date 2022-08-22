#!/usr/bin/env python
# coding: utf-8

# Q1.Assign a variable to a any number 
# Multiply the number by 3
#  Add 6 to the result from bullet 2
#  Divide ths number by 3
#  Subtract the number from byllet 1 from the abswer in buller 4
#  The answer is 2

# In[5]:



a = 8 
a = a * 3
a = a + 6
a = a / 3
a = a - 8
a


# In[46]:


a = input() // when we take input() it generally takes inputs as String , then we need to convert it to integer.
a=int (a)
a = a * 3
a = a + 6
a = a / 3
a = a - 8
a


# In[45]:


type(a)


# In[ ]:


Type Conversion


# In[47]:


name = input("What is your name?")
print(f"Hello {name}!")
birth_year = input("What is your birth year ?")
print(f" You were born in {birth_year}.")


# Q.Input a value from the user and keep it in variable a
#   Input another value from the user and keep it in variable b
#   print the product of the two values (a * b)

# In[51]:


a = input()
a = int (a)
b = input()
b = int (b)
ans= a*b
print(ans)


# Q2.Input how many years the user it.
# Convert the years to an integer
# calculate how many days , hours , minutes and seconds since the user is

# In[9]:


age = input() # taking input from user  , its data type is 'str' 
age= int(age) # esxternally typecasting to integer
type (age)
days = age * 365 
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"No of days in {age} years are is {days} days" )
print(f"No of days in {age} years are is {days} days and total hours is {hours} hours" )
print(f"No of days in {age} years are is {days} days and total hours is {hours} hours and {minutes} minutes" )
print(f"No of days in {age} years are is {days} days and total hours is {hours} hours  and {minutes} minutes and {seconds} seconds in total")


# Q3.  Make a Calculator 
# 

# In[12]:


a = input()
int (a)
b = input()
int (b)

print("Enter your choice for calculations")
case = input()
int (case)
if (case == 1)
    ans = a+b
    print(f"Sum of two no is {ans}")
    
elif (case == 2)
    ans = a-b
    print(f"diff of two no is {ans}")
    
elif (case == 3)
    ans = a*b
    print(f"Pdt of two no is {ans}")
    
elif    (case == 4)
    ans = a/b
    print(f"division of two no is {ans}")
    
elif    (case == 5)
    ans = a%b
    print(f"Modulus of two no is {ans}")
    
elif    (6)
    ans = a**b
    print(f"Power of two no is {ans}")


# In[13]:


# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


# In[ ]:





# In[ ]:





# In[ ]:




