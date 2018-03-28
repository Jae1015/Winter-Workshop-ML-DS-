import numpy as np
import matplotlib.pyplot as plt

import csv

from numpy import loadtxt
key_value = loadtxt("filename.csv", delimiter=",")
mydict = { k:v for k,v in key_value }


data = np.loadcsv('@SrBachchan.csv')

# Choose how many bins you want here
num_bins = 20

# Use the histogram function to bin the data
counts, bin_edges = np.histogram(data, bins=num_bins, normed=True)

# Now find the cdf
cdf = np.cumsum(counts)

# And finally plot the cdf
plt.plot(bin_edges[1:], cdf)

plt.show()

