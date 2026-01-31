#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')
spam_words = ["win", "cash", "free", "prize"]
text = "You are WINNING a free prize now"
text = text.lower()
tokens = word_tokenize(text)
is_spam = any(word in tokens for word in spam_words)
print(is_spam)


# In[ ]:




