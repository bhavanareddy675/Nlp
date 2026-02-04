#!/usr/bin/env python
# coding: utf-8

# In[1]:


word_count={"apple":5, "banana":7, "cherry":3}
vocabulary=10
total=sum(word_count.values())

def calculate_laplace(word):
    count=word_count.get(word, 0)
    probability=(count + 1) / (total + vocabulary)
    return probability
new_word="cherry"
result=calculate_laplace(new_word)
print(result)


# In[ ]:




