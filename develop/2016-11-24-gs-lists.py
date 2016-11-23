
# coding: utf-8

# # Lists
# 
# Declaring lists is quite efficient as O(1)

# In[1]:

small_list = [i for i in range(10)]
large_list = [i for i in range(100000000)]


# In[2]:

get_ipython().magic('timeit -qo small_list[1]')


# In[3]:

get_ipython().magic('timeit -qo large_list[1000000]')


# ## O(1) operations on Lists

# In[4]:

l = list(small_list)
print(l)


# In[5]:

l[0] = 100
print(l)


# In[6]:

len(l)


# In[7]:

l.append(100)
print(l)


# In[8]:

l.pop()
print(l)


# In[9]:

l.clear()
print(l)


# ## O(n) operations on Lists

# In[10]:

l = list(small_list)
print(l)


# In[11]:

l[1:2] = [0,0] 
print(l)


# In[12]:

del l[0]
print(l)


# In[13]:

l.remove(0)
print(l)


# In[14]:

l.pop(0)
print(l)


# In[15]:

for i in l:
    print(i)


# In[ ]:



