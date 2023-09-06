#!/usr/bin env python3

##### Assigning words to transitions created in main.R #####

# imports
import pandas as pd
from itertools import chain

# create pandas df and extract indices
df = pd.read_csv('indices.csv')
wordidx = list(df["x"])

# word variables
w1 = ["pi", "tu", "bi"]
w2 = ["bu", "pa", "da"]
w3 = ["di", "ba", "pu"]
w4 = ["ta", "ti", "tu"]

# create empty list
wordlist = []

# replace 
for i in wordidx:
    if wordidx[i] == 1:
        wordlist.append(w1)
    elif wordidx[i] == 2:
        wordlist.append(w2)
    elif wordidx[i] == 3:
        wordlist.append(w3)
    elif wordidx[i] == 4:
        wordlist.append(w4)

# unlist and write to csv
wordlist = pd.DataFrame(list(chain.from_iterable(wordlist)))
wordlist.to_csv('wordlist.csv')
