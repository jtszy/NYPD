import numpy as np

data = np.load('sample_treated.npz')
lst = data.files
print(lst)

min = 0
min_value = 0

outputs = data["outputs"]
for i in range(len(outputs)):
    if abs(outputs[i][-1]/outputs[i][0] - 2) < abs(min-2):
        min = outputs[i][-1]/outputs[i][0]
        min_value = i

print("object ", min_value, " grow its size ", min, " times")
