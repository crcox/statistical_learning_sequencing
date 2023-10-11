# imports
import numpy as np
import csv
import random
from itertools import chain

# list of syllables
syllables = ["di", "da", "du", "pi", "pa", "pu", "bi", "ba", "bu", "ti", "tu", "ta"]

# create TPM
randTPM = np.full((12, 12), fill_value=(1/11))
np.fill_diagonal(randTPM, 0)
print(randTPM)

# begin creating orders
numstim = 288 # 288 total syllable presentations
initstate = np.random.choice(range(12))  # Random initial state
order = [syllables[initstate]]
current_state = initstate

while len(order) < numstim:
    next_state = np.random.choice(range(12), p=randTPM[current_state])
    if syllables[next_state] != order[-1]:
        order.append(syllables[next_state])
        current_state = next_state

# print orders
print(order)
print(order[::-1]) # order 2 = order 1 in reverse

# ouptut orders to .csv
filename = "random_orders.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Order 1", "Order 2"])
    writer.writerows(zip(order, order[::-1]))

################### Trying another way ###################

# list of syllables
syllables = ["di", "da", "du", "pi", "pa", "pu", "bi", "ba", "bu", "ti", "tu", "ta"]

# generate orders
numstim = 48
anotherorder = []

for i in range(numstim):
    anotherorder.append(random.sample(syllables, k=len(syllables)))

another1 = list(chain.from_iterable(anotherorder))
another2 = list(chain.from_iterable(anotherorder[::-1]))

# ouptut orders to .csv
filename = "another_random.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Order 1", "Order 2"])
    writer.writerows(zip(another1, another2))