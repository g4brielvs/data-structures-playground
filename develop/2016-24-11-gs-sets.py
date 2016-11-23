
# coding: utf-8

# # Sets

# In[1]:

s = {0, (1, 2), 'a'}
print(s)


# ## Operations on Sets

# In[2]:

numbers = {1, 2, 3, 4}
lists = {(1,2), (3, 4)}
letters = {'a', 'b', 'c', 'd'}


# In[3]:

len(numbers)


# In[4]:

1 in numbers


# In[5]:

(0, 0) not in lists


# In[6]:

numbers.issubset(lists) # numbers <= lists


# In[7]:

numbers.issuperset(letters) # numbers >= letters


# In[8]:

union = numbers.union(lists) # numbers | lists
print(union)


# In[9]:

intersection = numbers.intersection(letters) # numbers & letters
print(intersection)


# In[10]:

difference = numbers.difference(lists) # numbers - lists
print(difference)


# In[11]:

symmetric_difference = numbers.symmetric_difference(letters) # numbers ˆ letters
print(symmetric_difference)


# In[12]:

copy = numbers.copy()
print(copy)


# In[ ]:



