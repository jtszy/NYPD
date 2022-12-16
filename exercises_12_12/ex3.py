import csv
import os
import numpy as np

data = np.load('ex3_data.npy')
count = [0]*4

print(data.shape)

res = np.array([[0,0,0,0]])

for x in data:
    is_nan = False
    for i in range(4):
        if np.isnan(x[i]):
            count[i] += 1
            is_nan = True
    if not is_nan:
        res = np.concatenate((res,[x]),axis = 0)


res = res[1:][:]
print(res.shape)
print(count)



