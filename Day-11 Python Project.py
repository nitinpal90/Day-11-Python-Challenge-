#!/usr/bin/env python
# coding: utf-8

# # Day-11 Python Project

# # Creating a Set

# In[1]:


a = {"BCA", "MBA", "MCA"} ## Set items are not allow the indexes' numbers
print(a)
print(type(a))


# # Set not allowed duplicates

# In[2]:


a = {"BCA", "MBA", "MCA", "BCA", "MBA", "MCA"}
print(a)
print(type(a))


# # True and 1 is consider is same value

# In[3]:


a = {"BCA", "MBA", "MCA", "BCA", "MBA", "MCA", 1, 2, 3, True}
print(a)


# # Lenght Function

# In[5]:


a = {"BCA", "MBA", "MCA"}
print(len(a))


# # Data types in set

# In[7]:


x1 = {1,2,3,4} ## Int Data Type
x2 = {1.2,1.3,1.4,1.5}  ## Float Data Type
x3 = {"a", "b","c"} ## String Data Type
x4 = [True, False, True] ## Boolean Data type
x5 = x1,x2,x3,x4
print(x5)


# In[8]:


a = {1, "A", 1.2, True, 2+3j}
print(a)


# # Set Constructor

# In[10]:


a = set(("A", "B", "c"))
print(a)
print(type(a))


# # Creating Empty Set

# In[11]:


a = set()
print(a)
print(type(a))


# # Access Items

# In[13]:


a = {"A", "B", "C", "D"}

for x in a:
    print(x)


# # Check Items

# In[15]:


check = {"a", "b", "c", "d"}
print("b" in check)


# In[16]:


check = {"a", "b", "c", "d"}
print("e" in check)


# # Add Function

# In[21]:


a = {"a", "b", "c", "d"}
a.add("e")
print(a)


# # Update Function

# In[25]:


a = {"A", "B", "C"}
b = {1,2,3,5,6,7}
a.update(b)
print(a)


# # Remove Function

# In[26]:


a = {1, 2, 3, 5, 6, 7, 'A', 'C', 'B'}
a.remove('A')
print(a)


# # Pop Functions

# In[27]:


a = {1, 2, 3, 5, 6, 7, 'C', 'B'} ## Pop function use to delete random numbers in present set
b = a.pop()
print(a)


# # Clear Function

# In[28]:


a = {1, 2, 3, 5, 6, 7, 'C', 'B'} ## Clear function use to clear all the content of the present set
a.clear()
print(a)


# # Write a programe to find the maximum and minimum value of a present set

# In[32]:


a = {1,2,3,45,76,89,23,45,67,87}
print("Present Set is")
print(a)
print("The maximum value in the present set")
print(max(a))
print("The minimum value in the present set")
print(min(a))
print("Total Sum of the present set")
print(sum(a))


# # Return a new set of identical items from two sets

# In[33]:


a = {10,20,30,40,50}  ## Show the common value of the present set
b = {10,30,70,90,80}

c = a.intersection(b)
print(c)


# # Practice Question 

# In[37]:


a = {1,2,3,4,5,6,7,89,9}
print(len(a))
print(sum(a))
print(max(a))
print(min(a))
b = set(a)
print(type(b))

