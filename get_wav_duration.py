########## getting duration of sounds ##########

# imports
import wave
import contextlib
import os
import pandas as pd


user = os.path.expanduser('~')
sound_dir = str(f'{user}/Desktop/sounds/')
sound_files = os.listdir(sound_dir)

#remove .DS_store
sound_files.remove('.DS_Store')
sound_files.remove('main.py')
print(sound_files)

# loop through files and get their lengths
sounds = pd.DataFrame(columns=['name', 'duration'])
sounds['name'] = sound_files
sound_lens = []

for i in range(len(sound_files)):
    with contextlib.closing(wave.open(sound_files[i],'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        sound_lens.append(round(duration,4))


sounds['duration'] = sound_lens

# load in word list
wordlist = pd.read_csv(f'{user}/Box Sync/willdecker/LSU Undergrad/Honors-Thesis/github/statistical_learning_sequencing/wordlist.csv')
print(wordlist["0"][1])


durs = []
for i in range(len(wordlist["0"])):
    for j in range(len(sounds["name"])):
        stem = sounds['name'][j].split('.')
        if wordlist["0"][i] == stem[0]:
            durs.append(sounds['duration'][j])
            
wordlist["durs"] = durs

wordlist.to_csv('s_1_wordlist.csv')