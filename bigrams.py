#!/usr/bin/env python
# coding: utf-8

# In[3]:


import nltk
from collections import Counter

word_counts = {
    "the": 5000,
    "tea": 2000,
    "team": 1000,
    "ten": 200
}

summ = sum(word_counts.values())

def edit_distance(wrong_input, w):
    distance = nltk.edit_distance(w, wrong_input)
    if distance == 0:
        return 1.0
    return 1 / (10 ** distance)

def prior_probability(w):
    return word_counts.get(w, 0) / summ
    

def suggested(wrong_input):
    candidates = list(word_counts.keys())
    correct_word = None
    high_prob = -1

    for w in candidates:
        likelihood = edit_distance(wrong_input, w)
        prior = prior_probability(w)
        result = likelihood * prior

        if result > high_prob:
            high_prob = result
            correct_word = w

    return correct_word  

wrong_input = "teama"
correction = suggested(wrong_input)
print(correction)


# In[4]:


from nltk import bigrams
from collections import Counter

text = "i love pizza i love cake i hate vegetables"
tokens = text.split()

bi_list = list(bigrams(tokens))
bi_count = Counter(bi_list)

res = {pair[1]: count for pair, count in bi_count.items() if pair[0] == 'i'}
print(res)

