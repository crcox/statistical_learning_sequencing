#!/usr/bin env python3

##### Assigning words to transitions created in main.R #####

# imports
import pandas as pd
from itertools import chain
import os
import wave
import contextlib

_thisDir = os.path.dirname(os.path.abspath(__name__))

x = str(_thisDir + '/filename')

# create pandas df and extract indices
df = pd.read_csv('indices.csv')
wordidx = df["x"]

# word variables
w1 = ["pi", "tu", "bi"]
w2 = ["bu", "pa", "da"]
w3 = ["di", "ba", "pu"]
w4 = ["ta", "ti", "du"]

wordset = (w1, w2, w3, w4)
# create empty list
wordlist = []

# replace 
for i in range(len(wordidx)):
    if wordidx[i] == 1:
        wordlist.append(w1)
    elif wordidx[i] == 2:
        wordlist.append(w2)
    elif wordidx[i] == 3:
        wordlist.append(w3)
    elif wordidx[i] == 4:
        wordlist.append(w4)

# unlist and write to csv

word_list1 = wordlist
word_list2 = wordlist[::-1]
s_1_wordlist = pd.DataFrame(list(chain.from_iterable(word_list1)))
s_2_wordlist = pd.DataFrame(list(chain.from_iterable(word_list2)))
s_1_wordlist.to_csv('/Volumes/WILLUSB/DECKER/exposure/s_1_wordlist.csv')
s_2_wordlist.to_csv('/Volumes/WILLUSB/DECKER/exposure/s_2_wordlist.csv')





########## getting duration of sounds ##########
user = os.path.expanduser('~')
sound_dir = str(f'{user}/Desktop/sounds/')
sound_files = os.listdir(sound_dir)

#remove .DS_store
sound_files.remove('.DS_Store')
print(sound_files)

# add path
for i in range(len(sound_files)):
    sound_files[sound_dir + sound_files[i]]

# loop through files and get their lengths
sound_lens = pd.DataFrame

for i in range(len(sound_files)):
    with contextlib.closing(wave.open(sound_files[i],'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        print(duration)




###########################

import pandas as pd

mine = pd.read_csv('/Volumes/WILLUSB/DECKER/exposure/s_1_wordlist.csv')

mine['word']
mine['durs']

x = pd.DataFrame()
x['word'] = mine['word'][::-1]
x['durs'] = mine['durs'][::-1]

x.to_csv('/Volumes/WILLUSB/DECKER/exposure/s_2_wordlist.csv')

