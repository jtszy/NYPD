import numpy as np

data = np.genfromtxt("iris.csv", delimiter = ',',skip_header=1, )

data = np.delete(data,-1,1)

print("mean: ", np.mean(data,axis = 1))
print("median: ", np.median(data,axis = 1))
print("std: ", np.std(data, axis = 1))
