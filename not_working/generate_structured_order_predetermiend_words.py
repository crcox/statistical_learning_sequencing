# import numpy and csv
import random
from itertools import chain
import numpy as np
import csv

# words
words = [['pi', 'tu', 'bi'], ['bu', 'pa', 'da'], ['di', 'ba', 'pu'], ['ta', 'ti', 'du']]

# create order
numstim = 48
order = []
for i in range(numstim):
    order.append(random.sample(words, k=len(words)))

# print orders
order1 = list(chain.from_iterable(order))
order2 = list(chain.from_iterable(order[::-1]))
order1_output = list(np.concatenate(order1))
order2_output = list(np.concatenate(order2))


# un embed words as list and ouptut orders to .csv
filename = "structured_orders_predetermined_words.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Order 1", "Order 2"])
    writer.writerows(zip(order1_output, order2_output))

# check word count
for i in range(len(words)):
    order1.count(words[i])


