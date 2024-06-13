import matplotlib.pyplot as plt 
import numpy as np 
import random

data = []
another_data = []
fig = plt.figure()

for i in range(100):
    data.append(int(random.random()*100)%100)
    another_data.append(int(random.random()*100)%100)



counts, bins = np.histogram(data)
plt.stairs(counts, bins)
plt.hist(bins[:-1], bins, weights=counts)

plt.subplot(1,2,1)
plt.plot(range(0,100), data)

plt.subplot(1,2,2)
plt.plot(range(0,100), data)

plt.show()