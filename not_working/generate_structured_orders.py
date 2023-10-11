# import numpy and csv
import numpy as np
import csv

# list of syllables
syllables = ["di", "da", "du", "pi", "pa", "pu", "bi", "ba", "bu", "ti", "tu", "ta"]

# create words using TPM
strucTPM = np.zeros((12, 12))
strucTPM[0, 1] = 1
strucTPM[1, 2] = 1
strucTPM[2, range(0, 12, 3)] = 0.25
strucTPM[3, 4] = 1
strucTPM[4, 5] = 1
strucTPM[5, range(0, 12, 3)] = 0.25
strucTPM[6, 7] = 1
strucTPM[7, 8] = 1
strucTPM[8, range(0, 12, 3)] = 0.25
strucTPM[9, 10] = 1
strucTPM[10, 11] = 1
strucTPM[11, range(0, 12, 3)] = 0.25

# create orders
numstim = 288
initstate = np.random.choice(range(12))  # Random initial state
order = [syllables[initstate]]
current_state = initstate

while len(order) < numstim:
    next_state = np.random.choice(range(12), p=strucTPM[current_state])
    if syllables[next_state] != order[-1]:
        order.append(syllables[next_state])
        current_state = next_state

# print orders
order1 = order
order2 = order[::-1] # order 2 = order 1 in reverse
print(order1)
print(order2)

# ouptut orders to .csv
filename = "structured_orders.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Order 1", "Order 2"])
    writer.writerows(zip(order, order[::-1]))
